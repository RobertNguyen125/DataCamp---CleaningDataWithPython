# NOTE: the data from datacamp is different from gapminder.csv used in this so some codes might not work

import pandas as pd
import matplotlib.pyplot as plt

gapminder = pd.read_csv('/Users/apple/desktop/cleaningDataPython/gapminder.csv')

gapminder.plot(kind='scatter',x='1800', y='1899')

# label x,y axis
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# plt.show()

# The graph show there are many countries on the diagonal line -> data might not be collected during those times


# function that takes a row of data, drop all the missing value and check if the remaining value  is
# greater than or equal 0
def check_null_or_valid(row_data):
    no_na = row_data.dropna()
    numeric = pd.to_numeric(no_na)
    ge0 = numeric > 0
    return ge0
# check if the first column is 'Life expectancy'
# assert gapminder.columns[0]=='Life expectancy'

#check whether the values  in the row are valid
# NOTE: use all().all() to apply this to the entire DataFrame
assert gapminder.iloc[:,1:].apply(check_null_or_valid, axis=1).all().all()

# check if there is 1 instance in each country
assert gapminder['Life expectancy'].value_counts()[0]=1
