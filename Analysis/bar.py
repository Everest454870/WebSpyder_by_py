# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

df = pd.read_csv("car_message.csv", encoding="utf-8")

df['上牌日期'] = df['上牌日期'].replace('未上牌', pd.NaT)
df['上牌日期'].fillna(pd.to_datetime('1990-01', format='%Y-%m'), inplace=True)
df['上牌日期'] = pd.to_datetime(df['上牌日期'], format='%Y-%m')

bins = pd.date_range(start=df['上牌日期'].min(), end='2025-01-01 00:00:00', freq='YS')
print("---------",df['上牌日期'].min())
labels = pd.date_range(start=df['上牌日期'].min(), periods=len(bins)-1,freq='YS')

df['日期区间'] = pd.cut(df['上牌日期'], bins=bins, labels=labels, right=False)
grouped = df.groupby('日期区间').size()
print(grouped)

#以下绘制柱状图
rcParams['font.sans-serif'] = ['SimHei']
x = ['未上牌','1991','1992','1993','1994','1995','1996','1997','1998','1999',
     '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
     '2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021',
     '2022','2023','2024']
y = grouped.values
plt.figure(450)
plt.figure(figsize=(7,5))
plt.title('上牌年份')
plt.bar(x,y,color='#ff0000')
plt.xticks(fontsize=5)
for i, v in enumerate(y):
    plt.text(i, v + 0.2, str(v), ha='center', va='bottom', fontsize=10)
plt.savefig('bar.png')
plt.show()


