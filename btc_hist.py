# bitcoin historical data
#%%
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

        
df = pd.read_csv(r"path in your computer") #reading the data (csv)             


df.columns = [each.lower() for each in df.columns]
df.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in df.columns]  #this is a necessary regulation to avoid syntax difficulties

 #creating and checking a feature called "date_time" to be able to read time instead of timestamp
df["date_time"] = df.timestam
df['date_time'] = pd.to_datetime(df['date_time'],unit='s')
print(df.date_time.tail())             

 #inserting the filters to seperate 2 bull runs
filter1 = df.open<1100
filter2 = df.open>3
first_bull = df[filter1 & filter2]
filter3 = df.open>1100
filter4 = df.open<10000
second_bull = df[filter3 & filter4]            

#plotting the graph to see the behavoir of price visually
plt.plot(first_bull.date_time,first_bull.open,color = "green",alpha = 0.7,label = "first")
plt.plot(second_bull.date_time,second_bull.open,color = "red",alpha = 0.5,label = "second")
plt.xlabel("date")
plt.ylabel("price")
plt.legend(loc = "best")
plt.show()     

#preparation phase to seperation 2 bull runs to analyze in different aspects
print(df[df["date_time"]== "2011-11-21 00:10:03"].index.values)
print(df[df["date_time"]== "2013-11-25 00:00:00"].index.values)
print(df[df["timestamp"]== 1440363600].index.values)
print(df[df["timestamp"]== 1514754000].index.values)    

#converting
from datetime import datetime, date
date_string = "01/01/2018"
date = datetime.strptime(date_string, "%m/%d/%Y")
timestamp = datetime.timestamp(date)
print(timestamp)        

#filtering
fb_vol = df[0:1000328]
sb_vol = df[1910956:3150796]   

#plotting the graph of 2 bull runs to inspect their BTC volume differentiation
plt.plot(fb_vol.date_time,fb_vol["volume_(btc)"],alpha = 0.5,color = "red",label = "first bull")
plt.plot(sb_vol.date_time,sb_vol["volume_(btc)"],alpha = 0.5,color = "green",label = "second bull")
plt.xlabel("date")
plt.ylabel("volume (BTC)")
plt.legend(loc="best")
plt.show() 

#plotting scatter type of graph to see the interaction/similarities
print(df.columns)
plt.scatter(fb_vol.close,fb_vol["volume_(btc)"],color = "red",alpha = 0.1,label = "price action")
plt.scatter(sb_vol.close,sb_vol["volume_(btc)"], color = "g",alpha = 0.1, label = "second price act")
plt.legend()
plt.xlabel("price")
plt.ylabel("volume (btc)")
plt.show()

#finding means of the volumes in a given period of time (2 bull runs) the gap between 2 mean volumes helps us to interpret easily whether if people still hodl*s BTC   
mean_vol_f = fb_vol["volume_(btc)"].mean()
mean_vol_s = sb_vol["volume_(btc)"].mean()
print(mean_vol_f)
print(mean_vol_s)
diff_vol = mean_vol_f - mean_vol_s
print(diff_vol)

#visualizing the volumes
plt.bar(1,height = mean_vol_f,color = "g",alpha = 0.5,label = "first bull vol mean")
plt.bar(2,height = mean_vol_s,color = "red",alpha = 0.1,color = "r",label="second bull vol mean")
plt.ylabel("mean vol 2")
plt.xlabel("mean vol 1")
plt.legend(loc = "best")
plt.show()


