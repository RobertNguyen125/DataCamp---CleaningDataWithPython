import pandas as pd
gapminder = pd.read_csv('/Users/apple/desktop/cleaningDataPython/gapminder.csv')

gapminder_melt = pd.melt(gapminder, id_vars='Life expectancy')

gapminder_melt.columns = ['country', 'year', 'life expectancy']

print(gapminder_melt.head())

#check data type

print(gapminder_melt.info())
