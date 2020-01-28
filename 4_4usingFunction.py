import pandas as pd
import numpy as np
import re

tips = pd.read_csv('/Users/apple/desktop/cleaningDataPython/tips.csv')

def recode_gender(gender):
    if gender == 'Female':
        return 1
    elif gender == 'Male':
        return 0
    else:
        return np.nan

tips['recode'] = tips.sex.apply(recode_gender)

print(tips.head())
