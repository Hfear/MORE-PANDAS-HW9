"""Use eval() to perform arithmetic operations on DataFrame columns.
Compare performance of eval() vs standard operations.
Use query() to filter large DataFrames efficiently.
Benchmark common operations with %timeit.
Optimize memory usage using categorical and appropriate numeric dtyp"""

import pandas as pd
import numpy as np

x = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

y = x.eval('C = A + B')
print("\nDataFrame with eval (y):")
print(y)

z = x['A'] + x['B']
print("\nDataFrame with standard operation (z):")
print(z)

big_data = pd.DataFrame({
    'A': np.random.randint(1, 100, size=1000000),
    'B': np.random.randint(1, 100, size=1000000)
})

filtered_data = big_data.query('A > 50 and B < 30')
print("\nFiltered large DataFrame using query (filtered_data):")
print(filtered_data)

# Benchmarking with %timeit
# %timeit x['A'] + x['B']  # Uncomment this line to benchmark

# Optimize memory using categorical and numeric dtype
big_data['A'] = big_data['A'].astype('category')
big_data['B'] = big_data['B'].astype('int16')
print("\nOptimized DataFrame (big_data):")
print(big_data)
