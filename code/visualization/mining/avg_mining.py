import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mpld3
import warnings
import matplotlib.dates as mdates
import datetime

warnings.filterwarnings('ignore')

css = """
table
{
  border-collapse: collapse;
}
table, th, td
{
  padding: 5px;
  border: 1px solid black;
  text-align: left;
  background-color: #FFFFFF;
}
"""

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
df = df[['close-approach-date', 'mining-index', 'object', 'minimum-AU-distance-normalized', 'v-relative']]

years = range(2025, 2201)
averages = []

for year in years:
    first_date = str(year)+'-01-01'
    last_date = str(year)+'-12-31'
    df_copy = df[(df['close-approach-date'] >= first_date) & (df['close-approach-date'] <= last_date)]
    averages.append(float('{0:.5f}'.format(df_copy['mining-index'].mean())))

fig, ax = plt.subplots(subplot_kw=dict(axisbg="#FFFFFF"), figsize=(15,7))
ax.text

scatter = ax.scatter(years, averages, c=averages, s=30)
ax.set_xlabel('Year', fontsize=18)
ax.set_ylabel('Average Extraction Index', fontsize=18, family='sans-serif', weight='bold')
ax.set_title('Average Element Extraction Index by Year', fontsize=24)
#ax.set_xlim(datetime.date(year, 1, 1), datetime.date(year, 12, 31))
ax.set_ylim(0.2, 0.3)

ax.tick_params(axis='both', which='major', pad=15, labelsize=10)
#df_copy['formatted'] = df_copy.index
#df_copy['formatted'] = df_copy['formatted'].apply(lambda x: x.strftime('%b %d, %Y'))
labels = ['<table><tr><th>Year</th><td>{0}</td></tr><tr><th>Average</th><td>{1}</td></table>'.format(i[0], i[1]) for i in zip(years, averages)]
tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels=labels, css=css)
mpld3.plugins.connect(fig, tooltip)
mpld3.save_html(fig, 'avg_scatter')
#mpld3.show()
