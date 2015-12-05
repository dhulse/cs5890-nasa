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

for year in range(2025, 2201):
    first_date = str(year)+'-01-01'
    last_date = str(year)+'-12-31'
    df_copy = df[(df['close-approach-date'] >= first_date) & (df['close-approach-date'] <= last_date)]
    df_copy.set_index(['close-approach-date'], inplace=True)
    fig, ax = plt.subplots(subplot_kw=dict(axisbg="#FFFFFF"), figsize=(15,7))
    ax.text

    scatter = ax.scatter(df_copy.index, df_copy['mining-index'], c=df_copy['mining-index'], s=30)
    ax.set_xlabel('Month', fontsize=18)
    ax.set_ylabel('Mining Index', fontsize=18, family='sans-serif', weight='bold')
    ax.set_title('Mining Asteroids in ' + str(year), fontsize=24)
    ax.set_xlim(datetime.date(year, 1, 1), datetime.date(year, 12, 31))
    ax.set_ylim(0.0, 1.0)

    ax.tick_params(axis='both', which='major', pad=15, labelsize=10)
    df_copy['formatted'] = df_copy.index
    df_copy['formatted'] = df_copy['formatted'].apply(lambda x: x.strftime('%b %d, %Y'))
    labels = ['<table><tr><th>Object</th><td>{0}</td></tr><tr><th>Velocity</th><td>{1} km/s</td></tr><tr><th>Distance</th><td>{2} AU</td></tr><tr><th>Date</th><td>{3}</td></tr></table>'.format(i[0], i[1], i[2], i[3]) for i in df_copy[['object', 'v-relative', 'minimum-AU-distance-normalized', 'formatted']].as_matrix()]
    tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels=labels, css=css)
    mpld3.plugins.connect(fig, tooltip)
    mpld3.save_html(fig, str(year)+'_scatter')
    #mpld3.show()

