# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:22:07 2020

@author: debdi
"""
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv (r'D:\AccidentsResearchProject\Data\US_Accidents_June20.csv')


df = data[(data.Severity >= 3)]

df.City.value_counts()[:30].plot(kind='pie', autopct="%1.1f%%")

plt.axis('equal')
plt.show()

temp = df['Start_Time'].str.split(" ",expand=True)
df['date'] = temp[0]
df['Time'] = temp[1]

from tqdm import tqdm
num = []
for i in range(0,24):
    num.append(i)
i=0
j=1
count = []

for i in tqdm(range(len(num)-1)):
    
    if i < 9:
       
        hour_start = '0'+str(i)+":"+'00'+':'+"00"
        hour_end = '0'+str(j)+":"+'00'+':'+"00"
        count.append(len(df[(df['Time']>=hour_start)&(df['Time']<=hour_end)]))
    
    elif i==9:
            hour_start = '0'+str(i)+":"+'00'+':'+"00"
            hour_end = str(j)+":"+'00'+':'+"00"
            count.append(len(df[(df['Time']>=hour_start)&(df['Time']<=hour_end)]))
            
            
    else:
        hour_start = str(i)+":"+'00'+':'+"00"
        hour_end = str(j)+":"+'00'+':'+"00"
        count.append(len(df[(df['Time']>=hour_start)&(df['Time']<=hour_end)]))
        
    i = j;
    j = i+1;
    
    
hour = []
for i in range(len(count)):
    hour.append(i)
X = hour
y = count

sns.set(style="whitegrid")
fig = plt.figure()
ax = fig.add_axes([0,0,2,2])
ax = sns.barplot(x=X, y=count)


df['Start_Time'] = pd.to_datetime(df['Start_Time'], format="%Y/%m/%d %H:%M:%S")
df['DayOfWeekNum'] = df['Start_Time'].dt.dayofweek
df['DayOfWeek'] = df['Start_Time'].dt.dayofweek
df['MonthDayNum'] = df['Start_Time'].dt.day
df['HourOfDay'] = df['Start_Time'].dt.hour

df.head()

fig, ax=plt.subplots(figsize=(16,7))
df['DayOfWeek'].value_counts(ascending=False).plot.bar(width=0.5,edgecolor='k',align='center',linewidth=2)
plt.xlabel('Day of the Week',fontsize=20)
plt.ylabel('Number of accidents',fontsize=20)
ax.tick_params(labelsize=20)
plt.title('Accident on Different Days of Week',fontsize=25)
plt.grid()
plt.ioff()