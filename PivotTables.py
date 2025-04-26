"""Build pivot tables with multiple levels for rows and columns.
Use margins=True to include subtotals in a pivot table.
Compare pivot tables with groupby and aggregation.
Write a function to generate customizable pivot tables
Use pivot tables to reshape and visualize sales or time-series data."""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie'],
    'Subject': ['Math', 'Math', 'English', 'English', 'Math', 'English'],
    'Exam': ['Midterm', 'Midterm', 'Final', 'Final', 'Midterm', 'Final'],
    'Score': [85, 78, 90, 82, 88, 91]
}

df = pd.DataFrame(data)

pivot_multi = pd.pivot_table(df, values='Score', index=['Student', 'Subject'], columns='Exam')
print(pivot_multi)

pivot_margins = pd.pivot_table(df, values='Score', index='Student', columns='Subject', margins=True)
print(pivot_margins)

grouped = df.groupby(['Student', 'Subject'])['Score'].mean().unstack()
print(grouped)

def make_pivot(index, columns, values='Score', aggfunc='mean', margins=False):
    return pd.pivot_table(df, index=index, columns=columns, values=values, aggfunc=aggfunc, margins=margins)

custom_pivot = make_pivot(index='Subject', columns='Exam', margins=True)
print(custom_pivot)

custom_pivot.plot(kind='bar', title='Average Scores by Subject and Exam')
plt.ylabel('Score')
plt.tight_layout()
plt.show()
