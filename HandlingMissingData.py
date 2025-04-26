"""Section – Handling Missing Data
Construct a DataFrame with missing values in multiple columns. Explore use of isnull(), dropna(), fillna().
Demonstrate forward fill, backward fill, and interpolation for time-indexed data.
Drop rows where a subset of columns have missing values.
Create a function that uses different fill strategies based on column dtype.
Evaluate how missing data affects statistical summaries and plotting."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

StudentInfo = {
    "Name": ["Hannah", "James", "Felix", np.nan, "Prince"],
    "Age": [np.nan, 39, 49, np.nan, 19],
}

df = pd.DataFrame(StudentInfo)
print(df)

print("is null funct \n", df.isnull())

print("drop missing values \n", df.dropna())

constantFill = df.fillna(0)
print("after constant fill \n",constantFill)

fowardFill = df.fillna(method="ffill")
print("after forward fill \n",fowardFill)

backwardFill = df.fillna(method="bfill")
print("after backward fill \n",backwardFill)

Interpolate = df.interpolate()
print("after interpolate \n",Interpolate)

print("drop rows where a subset of columns have missing values. \n", df.dropna(subset=["Age", "Name"]))

#function for diff fill types

print("summary after data filled \n", fowardFill.describe())

fowardFill["Age"].plot(kind="line", title="Age")
plt.show()





