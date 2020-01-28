import pandas as pd

airquality = pd.read_csv('/Users/apple/desktop/cleaningDataPython/airquality.csv')

# print(airquality.info()) 'Ozone' and 'Solar R.' columns have missing values

oz_mean = airquality.Ozone.mean()
airquality['Ozone']=airquality.Ozone.fillna(oz_mean)
print(airquality.info())
