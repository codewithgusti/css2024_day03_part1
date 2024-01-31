#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:30:46 2024

@author: dianachapter
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/dianachapter/css2024_day2/data_02/time_series_data.csv", index_col=0)
print(df.info())

df['Date'] =pd.to_datetime(df['Date'], format = "%Y-%m-%d")
print(df.info())

# plt.plot(df['Date'],df.['Temperature'])
# plt.ylabel("temp")
#


df['Temperature'].plot(kind='hist', bins=20, title='Temperature')
plt.show()