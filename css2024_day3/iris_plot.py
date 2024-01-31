#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:43:04 2024

@author: dianachapter
"""

import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("/Users/dianachapter/css2024_day2/data_02/iris.csv")

file["class"] = file["class"].str.replace("Iris-", "")

# plt.scatter(file["sepal_length"], file["petal_length"], )
# plt.xlabel("Sepal Length (cm)")
# plt.ylabel("Petal Length (cm)")
# plt.title("Iris Sepal-Petal Comparison")



class_count = file['class'].value_counts()
plt.pie(class_count,labels= class_count.index)
plt.show()