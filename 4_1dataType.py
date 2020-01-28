# astype() to convert type of a column
# df['treatment'] = df['treatment'].astype(str)
# df['sex'] = df['sex'].astype('category') since 'sex' is categorical
# df['treatment a'] =  pd.to_nuemric(df['treament a'],errors='coerce') convert all value to numeric
import pandas as pd
tips = pd.read_csv('/Users/apple/desktop/cleaningDataPython/tips.csv')

# print(tips.head())
# print(tips.info())

tips.sex = tips.sex.astype('category')
print(type(tips))
tips['sex'] = tips['sex'].astype('category')
tips['smoker'] = tips['smoker'].astype('category')
print(tips.info())
