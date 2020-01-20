import pandas as pd

df = pd.read_csv('/Users/apple/desktop/cleaningDataPython/dob_job_application_filings_subset.csv',low_memory=False)

print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)

# df_subset = pd.DataFrame(df[['Job #', 'Doc #', 'Borough', 'Initial Cost', 'Total Est. Fee', 'Existing Zoning Sqft', 'Proposed Zoning Sqft', 'Enlargement SQ Footage', 'Street Frontage', 'ExistingNo. of Stories',
#        'Proposed No. of Stories', 'Existing Height', 'Proposed Height']])

# Because the course will deal with the subset of 'dob_job_application_filings_subset.csv'
# so we create the subset
df_subset = df[['Job #', 'Doc #', 'Borough', 'Initial Cost', 'Total Est. Fee', 'Existing Zoning Sqft', 'Proposed Zoning Sqft', 'Enlargement SQ Footage', 'Street Frontage', 'ExistingNo. of Stories',
       'Proposed No. of Stories', 'Existing Height', 'Proposed Height']]

# Export dataframe subset to csv file
df_subset.to_csv('/Users/apple/desktop/cleaningDataPython/df_subset.csv')

df_subset = pd.read_csv('/Users/apple/desktop/cleaningDataPython/df_subset.csv')
print(df_subset.info())


# print(df_subset.head())
