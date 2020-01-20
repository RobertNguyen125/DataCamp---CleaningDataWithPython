import pandas as pd
tb = pd.read_csv('/Users/apple/desktop/cleaningDataPython/tb.csv')
# print(tb.head())
# print(tb.columns)

tb_melt = pd.melt(frame=tb, id_vars=['country','year'])
# print(tb_melt)

#create gender column
tb_melt['gender']=tb_melt.variable.str[0]

# create age group colum
tb_melt['age_group'] = tb_melt.variable.str[1:]

# print(tb_melt.head())

#ebola case: split a colum with .split() and .get()
ebola = pd.read_csv('/Users/apple/desktop/cleaningDataPython/ebola.csv')
# print(ebola.head())
# print(ebola.columns)

ebola_melt = pd.melt(frame=ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')
#print(ebola_melt)

ebola_melt['str_split']= ebola_melt['type_country'].str.split('_')
#print(ebola_melt.head())

ebola_melt['type'] = ebola_melt['str_split'].str.get(0)
ebola_melt['country'] = ebola_melt['str_split'].str.get(1)

#print(ebola_melt.head())
