# pd.concat([weather_p1, weather_p2], ignore_index=True) all data on top of the other and the index label is original
# so we need to reset the label by using ignore_index=True parameters in concat()

import pandas as pd
uber = pd.read_csv('/Users/apple/desktop/cleaningDataPython/nyc_uber_2014.csv')
# print(uber.info())
# print(uber.columns)

uber1 = uber.loc[0:98]
uber2 = uber.loc[99:197]
uber3 = uber.loc[198:]
# print(uber3.tail())

# print(uber2.info())

# uber1.to_csv('/Users/apple/desktop/cleaningDataPython/uber1.csv')
# uber2.to_csv('/Users/apple/desktop/cleaningDataPython/uber2.csv')
# uber3.to_csv('/Users/apple/desktop/cleaningDataPython/uber3.csv')

row_concat = pd.concat([uber1, uber2, uber3])
print(row_concat.shape)
print(row_concat.head())

# column Combination: use when we need to join 2 dataframe column by columns
# (or horizontal) rather than putting them on top of each other
# use the pd.concat() with the arguments axis=1 (axis=0 is default)
