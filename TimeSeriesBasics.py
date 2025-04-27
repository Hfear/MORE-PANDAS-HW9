"""Create a time-indexed Series and plot it.
Slice the time series by date range.
Resample the data to different frequencies.
Compute rolling statistics (mean, std).
Handle missing time points and perform interpolation."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""making time series"""

import pandas as pd
import numpy as np

dates = pd.date_range('2025-01-01', periods=10, freq='D')
timeSeries = pd.Series(np.random.randn(10), index=dates)

timeSeries.plot(figsize=(10, 5))
plt.title('Time-Indexed Series')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()

slice = timeSeries['2025-01-03':'2025-01-07']
print(slice)

GroupByWeek = timeSeries.resample('W').mean()
print(GroupByWeek)

mean = timeSeries.rolling(3).mean()
std  = timeSeries.rolling(3).std()

print(mean)
print(std)



