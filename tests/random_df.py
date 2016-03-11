import pandas as pd
import numpy as np

# define columns
cols = ['A', 'B', 'C']
# create a df with random values
df = pd.DataFrame(np.random.randn(10, 3), columns=cols)

print df

# track the rows to be deleted
rows_marked = list()


for idx, row in df.iterrows():
    if (idx+1) %3 == 0:
        rows_marked.append(idx)

#drop the rows defined in rows_marked
df = df.drop(rows_marked)

print df

tmp = df.xs(0)
tmp.name = 11
df = df.append(tmp)

print df
