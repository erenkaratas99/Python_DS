# bitcoin historical data
#%%
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

        
df = pd.read_csv(r"path in your computer") 

#%%
df.columns = [each.lower() for each in df.columns]
df.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in df.columns]
#%%

df["date_time"] = df.timestamp

df['date_time'] = pd.to_datetime(df['date_time'],unit='s')

print(df.date_time.tail())


#%%

filter1 = df.open<1100
filter2 = df.open>3

first_bull = df[filter1 & filter2]

filter3 = df.open>1100
filter4 = df.open<10000

second_bull = df[filter3 & filter4]

plt.plot(first_bull.date_time,first_bull.open,color = "green",alpha = 0.7,label = "first")
plt.plot(second_bull.date_time,second_bull.open,color = "red",alpha = 0.5,label = "second")
plt.xlabel("date")
plt.ylabel("price")
plt.legend(loc = "best")
plt.show()

#%%
print(df[df["date_time"]== "2011-11-21 00:10:03"].index.values)
print(df[df["date_time"]== "2013-11-25 00:00:00"].index.values)

#%%
print(df[df["timestamp"]== 1440363600].index.values)
print(df[df["timestamp"]== 1514754000].index.values)

#%%
from datetime import datetime, date
date_string = "01/01/2018"
date = datetime.strptime(date_string, "%m/%d/%Y")
timestamp = datetime.timestamp(date)
print(timestamp)
#%%
fb_vol = df[0:1000328]
sb_vol = df[1910956:3150796]

plt.plot(fb_vol.date_time,fb_vol["volume_(btc)"],alpha = 0.5,color = "red",label = "first bull")
plt.plot(sb_vol.date_time,sb_vol["volume_(btc)"],alpha = 0.5,color = "green",label = "second bull")
plt.xlabel("date")
plt.ylabel("volume (BTC)")
plt.legend(loc="best")
plt.show()
#%%
print(df.columns)
plt.scatter(fb_vol.close,fb_vol["volume_(btc)"],color = "red",alpha = 0.1,label = "price action")
plt.scatter(sb_vol.close,sb_vol["volume_(btc)"], color = "g",alpha = 0.1, label = "second price act")
plt.legend()
plt.xlabel("price")
plt.ylabel("volume (btc)")
plt.show()
#%%
mean_vol_f = fb_vol["volume_(btc)"].mean()
mean_vol_s = sb_vol["volume_(btc)"].mean()
#%%
df1 = df.copy()
df1["mean_vol1"]= mean_vol_f
df1["mean_vol2"]= mean_vol_s  


#%%
print(df1.mean_vol1.tail(1))
print(" ")
print(df1.mean_vol2.tail(1))
#%%
plt.bar(df1.date_time,df1.mean_vol1[2],alpha = 0.5,label = "first bull vol mean")
plt.bar(df1.date_time,df1.mean_vol2[2],alpha = 0.1,color = "r",label="second bull vol mean")
plt.ylabel("mean vol 2")
plt.xlabel("mean vol 1")
plt.legend(loc = "best")
plt.show()
#%%

