import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def normalize(df, column, new_column):
    minimum = df[column].min()
    maximum = df[column].max()
    df[new_column] = df[column].apply(lambda x: (x - minimum) / (maximum - minimum))

df = pd.read_csv('../data-set/space-objects-preprocess.csv')
df = df[['object', 'close-approach-date', 'v-relative', 'minimum-AU-distance']]

normalize(df, 'v-relative', 'v-relative-normalized')
normalize(df, 'minimum-AU-distance', 'minimum-AU-distance-normalized')

df['mining-index'] = .8 * df['v-relative-normalized'] + .2 * df['minimum-AU-distance-normalized'] # lower is better

df['close-approach-date'] = pd.to_datetime(df['close-approach-date'])
df['date_int'] = df['close-approach-date'].astype(np.int64)

graph = df[['date_int','mining-index']].as_matrix()
#print graph
#plt.scatter(graph[:,0], graph[:,1])
#plt.show()
