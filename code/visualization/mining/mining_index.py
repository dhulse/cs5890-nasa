import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mpld3
import warnings

warnings.filterwarnings('ignore')

def normalize(df, column, new_column):
    minimum = df[column].min()
    maximum = df[column].max()
    df[new_column] = df[column].apply(lambda x: (x - minimum) / (maximum - minimum))

df = pd.read_csv('../../../data-set/space-objects-preprocess.csv')
df = df[['object', 'close-approach-date', 'v-relative', 'minimum-AU-distance']]

normalize(df, 'v-relative', 'v-relative-normalized')
normalize(df, 'minimum-AU-distance', 'minimum-AU-distance-normalized')

df['mining-index'] = .8 * df['v-relative-normalized'] + .2 * df['minimum-AU-distance-normalized'] # lower is better

df['close-approach-date'] = pd.to_datetime(df['close-approach-date'], coerce=True)
#    df[(df['Date / Time'] >= '2000-01-01') & (df['Date / Time'] <= '2015-09-28') & (df['Date / Time'] != 'NaT')]
df = df[(df['close-approach-date'] >= '2025-01-01') & (df['close-approach-date'] < '2026-01-01')]
#df = df[df['mining-index'] < .16]
#df.set_index('close-approach-date')
print df.describe()
df['date_int'] = df['close-approach-date'].astype(np.int64)
df = df[['date_int', 'close-approach-date', 'mining-index', 'object', 'minimum-AU-distance-normalized', 'v-relative']]

fig, ax = plt.subplots(subplot_kw=dict(axisbg="#FFFFFF"))
scatter = ax.scatter(df['date_int'], df['mining-index'], c=df['mining-index'] * 100)

for i in df[['object', 'v-relative', 'minimum-AU-distance-normalized']].as_matrix():
    print i

labels = ['<h3>Object: {0}</h3><h3>Velocity: {1}</h3><h3>Distance AU: {2}</h3>'.format(i[0], i[1], i[2]) for i in df[['object', 'v-relative', 'minimum-AU-distance-normalized']].as_matrix()]

tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltip)
# try making one for each year and then writing it to HTML, from there we will load it as the webpages ask
mpld3.show()
