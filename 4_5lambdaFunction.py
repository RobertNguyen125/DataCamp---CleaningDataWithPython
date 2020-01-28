import pandas as pd
import re

tips = pd.read_csv('/Users/apple/desktop/cleaningDataPython/tips.csv')

tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$',''))
# print(tips.columns)
print(tips.head())

tips['total_dollar_re'] = tips.total_dollar.apply(lambda x : re.findall('\d+\.\d+',x)[0])
