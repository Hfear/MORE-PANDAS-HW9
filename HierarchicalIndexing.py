"""Create a MultiIndex from tuples and build a DataFrame indexed by it.
Slice and filter across multiple levels of a MultiIndex.
Swap and sort index levels using .swaplevel() and .sort_index().
Unstack and stack data, then reshape it back to original.
Use .groupby(level=...) on hierarchical data and apply aggregation."""

import pandas as pd
import numpy as np

multiIndex = pd.MultiIndex.from_tuples([(1,"A"),(2,"B"),(3,"C"),(4,"D"),(5,"E")],
                                       names = ['num', 'letter']
                                       )

dataFrame = { 'quantity' : [10,20,30,40,50]}
df = pd.DataFrame(dataFrame, index=multiIndex)
print(df)

print("filtered by B \n", df.xs('B', level='letter'))
print("filtered by num \n", df.xs(1,level = "num"))


swappedFrame = df.swaplevel()
print("swappedFrame \n", swappedFrame)

sortedFrame = df.sort_index(level='letter')
print("sortedFrame \n", sortedFrame)

unstackedFrame = df.unstack()
print("unstackedFrame \n", unstackedFrame)

stackedFrame = df.stack()
print("stackedFrame \n", stackedFrame)

groupedFrame = df.groupby(level = 'letter').agg(np.sum)
print("groupedFrame \n", groupedFrame)


