#df.column_name.value_counts(dropna=False): to count the missing value
# if dropna=True: it wont give you the frequency of missing data
# NOTE: can also use [] notation
#df[column_name].value_counts(dropna=False).head(): for first 5

#df.describe(): for data summary (mean, count, std etc.) so it is used for numeric values only

import pandas as pd
df = pd.read_csv('/Users/apple/desktop/cleaningDataPython/dob_job_application_filings_subset.csv');
df_sub = pd.read_csv('/Users/apple/desktop/cleaningDataPython/df_subset.csv')
# print(df_sub.head())
# print(df.head())

# print(df_sub['Borough'].value_counts(dropna=False));
# print(df['State'].value_counts(dropna=False));
# print(df['Site Fill'].value_counts(dropna=False));
