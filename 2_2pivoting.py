# the opposite process of melting to reshape data from analysis-friendly to reporting-friendly
# pivot_tidy = weather.pitovt(index = 'date', columns = 'element', values ='value')
# index: columns not to pivot
# columns: columns to pivot to new column
# values: fill the new columns

# pivot_table(): has a parameter that specifies how to deal with duplicate value
# E.g: aggreagate duplicate values by taking their average
# weather2_pivot = weather.pivot_table(values = 'value', index = 'date', columns = 'element'. aggfunc=np.mean)

import pandas as pd
print(airquality_melt.head())

airquality_pivot=airquality_melt.pivot_table(index=['Month', 'Day'], columns = 'measurement', values = 'reading')
print(airquality_pivot)

# the airquality_pivot df is not as the original. the df has hierarchical index 
# use reset_index() method to fix this issue

print(airquality_pivot.index) #to check airquality_pivot index
airquality_pivot_reset = airquality_pivot.reset_index()
print(airquality_pivot_reset.index) # to check airquality_pivot_reset after manipulation

# pivoting duplicate values
# airquality_dup was preloaded in Datacamp
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

print(airquality_pivot.head())

airquality_pivot = airquality_pivot.reset_index()

print(airquality_pivot.head())

print(airquality.head())
