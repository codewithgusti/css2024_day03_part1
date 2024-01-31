#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:08:26 2024

@author: dianachapter
"""

"""
Using matplotlib
"""

import matplotlib.pyplot as plt

# react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
# temp = [180, 200, 220, 240, 260]

# plt.plot(temp, react_conv)
# plt.xlabel("temperature")
# plt.ylabel("reaction cionversation")
# plt.title("chemical experiment")

# plt.show()

# day1_attendees = [70, 20 , 64, 90, 80]
# day1_names = ["blessing","mali", "pangi", "tafi" , "shini"]

# plt.bar(day1_names,day1_attendees)
# plt.show()

# x_scatter = [1 , 2 , 3, 4, 5]
# y_scatter = [2 , 4 , 6 , 8 , 10]

# plt.scatter(x_scatter, y_scatter)
# plt.show()

x_histogram = [1 ,2,2,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(x_histogram)
plt.show()