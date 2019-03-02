#!/usr/bin/env python

# class 6 homework
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = 'diabetes_data.txt'

# read file and load data
data = pd.read_csv(file, sep='\s+|,' ,header=0)
df = pd.DataFrame(data)

ncol = len(df.columns)

# write function to plot each feature of diabetes dataset
def plotter(feature):
    plt.plot(feature)

for i in range(0, ncol):
    fname = 'fig' + str(i) + '.png'
    plt.savefig(fname)

# intermediate: adding column headers
# names of column headers in a list
headers = ['Age', 'Sex', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'Y']

## commented out since header row already exists in dataset
#hdata = pd.read_csv(my_csv_file, sep='\s+|,' , headers)

# reach
# plotting BMI vs age and BP vs age on the same plot
fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 80)
ax1.plot(df[0], df[2], color='tab:red')

ax2 = ax1.twinx()
ax2.plot(df[0], df[3], color='tab:blue')

plt.savefig(mutliplot.png)
