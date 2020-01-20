#data visualisation can be useful to spot outlier
# bar plots for dicrete data value_counts
# histogram for continuous data counts
# box plots: visualise basic summary statistics: outlier, min/max, 25th, 50th, 75th percentiles

# import matplotlib.pyplot as plt
# df.column_name.plot('hist')

# data slicing:
# df[df.column > 100000000]: to filter the outliner

# df.boxplot(column = '', by = '')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# create histogram
df = pd.read_csv('/Users/apple/desktop/cleaningDataPython/dob_job_application_filings_subset.csv')
df_subset = pd.read_csv('/Users/apple/desktop/cleaningDataPython/df_subset.csv')
print(df['Existing Zoning Sqft'].describe())
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
# plt.savefig('/Users/apple/desktop/cleaningDataPython/1_3histogram.png')
# plt.show()


# create boxplot
df.boxplot(column='Initial Cost',by='Borough')
plt.show()

#create scatter plot
df.plot(kind='scatter', x='Initial Cost',y='Total Est. Fee',rot=70)
plt.show()
df_subset.plot(kind='scatter', x='Initial Cost',y='Total Est. Fee',rot=70)
# NOTE: result from 2nd plot shows there is a positive correlation between Initial Cost and Total Est. Fee
