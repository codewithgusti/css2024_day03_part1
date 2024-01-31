#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:52:10 2024

@author: dianachapter
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("poker_2016_09_27.csv", names = ["Time","NuN","x","y","z"])
df['Time'] =pd.to_datetime(df['Time'], format ='%H:%M:%S').dt.time

# plt.plot(df["Time"],df["x"],label= "x")
# plt.plot(df["Time"],df["y"],label= "y")
# plt.plot(df["Time"],df["z"],label= "z")

plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(df['Time'], df['NuN'], label='NuN')  # Plot NuN
plt.plot(df['Time'], df['x'], label='x')  # Plot x
plt.plot(df['Time'], df['y'], label='y')  # Plot y
plt.plot(df['Time'], df['z'], label='z')  # Plot z

# Set titles and labels
plt.title('Poker Data')
plt.xlabel('Time')
plt.ylabel('Values')

# Add legend
plt.legend()