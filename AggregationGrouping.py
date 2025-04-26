"""Group a dataset by one and two categorical columns and compute
multiple aggregates.
Use .agg() to apply custom functions per column.
Group by multiple keys and compute normalized statistics.
Use .filter() on groups based on a condition.
Combine groupby with sorting and visualization for grouped summaries."""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie'],
    'Subject': ['Math', 'Math', 'English', 'English', 'Math', 'English'],
    'Score': [85, 78, 90, 82, 88, 91]
}

df = pd.DataFrame(data)

print(df.groupby('Student')['Score'].mean())

print(df.groupby(['Student', 'Subject'])['Score'].agg(['count', 'mean']))

print(df.groupby('Subject')['Score'].agg(lambda x: x.max() - x.min()))

print(df.groupby('Subject').filter(lambda x: x['Score'].mean() > 85))

df.groupby('Subject')['Score'].mean().plot(kind='bar', title='Average Score by Subject')
plt.ylabel('Score')
plt.show()

