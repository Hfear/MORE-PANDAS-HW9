"""Convert between string dates and datetime objects.
Generate time ranges with custom frequency.
Demonstrate upsampling and downsampling.
Use asfreq() to set frequency explicitly.
Apply shifting and differencing operations."""

import pandas as pd
import numpy as np

StringDates = ['2025-01-01', '2025-02-15', '2025-03-20']
DateTimeDates  = pd.to_datetime(StringDates)
print(DateTimeDates)

weekly = pd.date_range('2002-01-01', '2002-12-31', freq='W')
daily  = pd.date_range('2002-01-01', '2002-01-31', freq='D')
print(weekly)
print(daily)

ts_weekly = pd.Series(np.random.randn(len(weekly)), index=weekly)
downsampled = ts_weekly.resample('M').mean()
upsampled = ts_weekly.resample('D').ffill()

print(downsampled)
print(upsampled.head())

asfreq_daily = ts_weekly.asfreq('D', method='ffill')
print(asfreq_daily.head())

shifted = ts_weekly.shift(1)
differenced = ts_weekly.diff(1)

print(shifted.head())
print(differenced.head())