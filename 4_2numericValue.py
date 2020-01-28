# if a column data type is 'object' instead of 'int/float', it means that there are non-numeric values
# pd.to_numeric() to convert the data type. If there are erros, we can ignore or coerce the value into NaN

import pandas as pd

tips = pd.read_csv('/Users/apple/desktop/cleaningDataPython/tips.csv')

# print(tips.info())
print(tips.head())

# the data for 'tip' and 'total_bill' from datacamp were object, so we will use the code below to convert them to to_numeric
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors = 'coerce')
tips['tip'] = pd.to_nuemric(tips['tip'], errors='coerce')

print(tips.head())
