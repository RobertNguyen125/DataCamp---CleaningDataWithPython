# Principles of Tidy Data
# - Column represent seperate variables
# - Rows represent individual observations
# - Observational unit form tables (not cover in this course)

# data format better for reporting vs analysing
# problems we are trying to fix: columns contain values instead of variables use pd.melt

# melt() turns columns into rows
# pd.melt(frame=df, id_vars='name', value_vars=['treatment a', 'treatment b'])
# id_vars: columns of data not to melt
# value_vars: columns to melt, if now value_vars, all columns not set in id_vars will be melt
# the dataset is airquality.csv

import pandas as pd

airquality = pd.read_csv('/Users/apple/desktop/cleaningDataPython/airquality.csv', index_col=0)
# print(airquality.head())
airquality_melt = pd.melt(frame=airquality, id_vars='Date')
print(airquality_melt.head()) # NOTE: inspect the melt version pf airquality_melt

# add meaningful names for melt()
airquality_melt = pd.melt(airquality, id_vars='Date', var_name='measurement', value_name='reading')
print(airquality_melt)
