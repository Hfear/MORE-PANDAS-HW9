"""Convert object columns to category dtype and observe memory usage.
Set and reorder category levels explicitly.
Perform comparisons and sorting on categorical columns.
Group by categorical variables and compute stats.
Use pd.get_dummies() to one-hot encode categorical feature"""

import pandas as pd

data = {'color': ['red', 'blue', 'green', 'blue', 'green', 'red', 'green'],
        'shape': ['circle', 'square', 'circle', 'circle', 'square', 'square', 'circle']}

df = pd.DataFrame(data)

df['color'] = df['color'].astype('category')
df['shape'] = df['shape'].astype('category')

memory_before = df.memory_usage(deep=True)
df['color'] = df['color'].cat.set_categories(['red', 'blue', 'green', 'yellow'])
df['shape'] = df['shape'].cat.set_categories(['circle', 'square', 'triangle'])

memory_after = df.memory_usage(deep=True)

df_sorted = df.sort_values(by='color')
grouped_stats = df.groupby('color').size()
hot_encoded = pd.get_dummies(df['shape'])

print(df)
print(memory_before, memory_after)
print(df_sorted)
print(grouped_stats)
print(hot_encoded)
