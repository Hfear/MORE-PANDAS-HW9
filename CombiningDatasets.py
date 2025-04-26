""" Combining Datasets
Merge two datasets on a shared column with inner and outer joins.
Concatenate DataFrames with keys to create a MultiIndex.
Join time-indexed DataFrames using .join(method='ffill').
Write a function to merge data from multiple sources with differing schemas.
Combine data with duplicate indices and demonstrate resolving conflicts."""

import pandas as pd
import numpy as np

frame1 = pd.DataFrame({
    'id': ['a', 'b', 'c', 'd'],
    'colors': ['red', 'green', 'blue', 'yellow']
})

frame2 = pd.DataFrame({
    'id': ['f', 'g', 'h', 'i'],
    'shape': ['square', 'circle', 'triangle', 'square']
})

innerMerged = pd.merge(frame1, frame2, on='id', how='inner')
print("inner merged: \n", innerMerged)

outerMerged = pd.merge(frame1, frame2, on='id', how='outer')
print("outer merged: \n", outerMerged)

frame3 = pd.DataFrame({
    'id': ['a', 'b', 'c', 'd'],
    'colors' : ['purple', 'lavender', 'blue', 'green']
}, index=[0, 1,2,3])

frame4 = pd.DataFrame({
    'id': ['f', 'e', 'c', 'z'],
    'colors' : ['orange', 'cyan', 'pink', 'green']
}, index=[4,5,6,7])

concatenated = pd.concat([frame3, frame4], keys=['a', 'b'])
print("concatenated: \n", concatenated)

timeIndex = pd.date_range('1/1/2018', periods=3)
frame5 = pd.DataFrame({
    'val': [1, np.nan,3]
}, index=timeIndex)

frame6 = pd.DataFrame({
    'val': [4, np.nan,7]
}, index=timeIndex)

joined = frame5.join(frame6)
joined = joined.ffill()
print("joined: \n", joined)



