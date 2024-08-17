# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math

df = pd.read_csv("car_message.csv",encoding="utf-8")
price_arr = df['报价'][:]
print("-------------------",type(df))
#print(df)
#print("-------------------",type(price_arr))
#print(price_arr)
#print(type(price_arr[4]))
Arr01 = []
Arr02 = []
Arr03 = []
Arr04 = []
Arr05 = []
Arr06 = []


# 将数据分到相应的区间
for i in price_arr:
    if math.isnan(i):
        continue  # 跳过nan值
    else:
        if 0<i and i<= 10:
            Arr01.append(i)
        elif 10<i and i<= 20:
            Arr02.append(i)
        elif 20<i and i<= 30:
            Arr03.append(i)
        elif 30<i and i<= 50:
            Arr04.append(i)
        elif 50<i and i<= 100:
            Arr05.append(i)
        else:
            Arr06.append(i)

print(f"Arr01 contains {len(Arr01)} items")
print(f"Arr02 contains {len(Arr02)} items")
print(f"Arr03 contains {len(Arr03)} items")
print(f"Arr04 contains {len(Arr04)} items")
print(f"Arr05 contains {len(Arr05)} items")
print(f"Arr06 contains {len(Arr06)} items")

rcParams['font.sans-serif'] = ['SimHei']
arr = [Arr01,Arr02,Arr03,Arr04,Arr05]
plt.figure(dpi=450)
plt.figure(figsize=(7,5))
plt.title('报价箱线图，低于百万（单位：万元)')
plt.boxplot(arr)
plt.savefig('boxplot_lower.png')
plt.show()

arr = [Arr06]
plt.figure(dpi=450)
plt.figure(figsize=(7,5))
plt.title('报价箱线图，高于百万（单位：万元)')
plt.boxplot(arr)
plt.savefig('boxplot_higher.png')
plt.show()
     


