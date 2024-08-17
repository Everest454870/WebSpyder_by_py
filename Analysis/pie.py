# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

df = pd.read_csv("car_message.csv",encoding="utf-8")
bins = [0,10,20,30,50,100,float("inf")]
labels = ['0-10','10-20','20-30','30-50','50-100','100万以上']
df['报价区间'] = pd.cut(df['报价'],bins=bins,labels=labels)
grouped = df.groupby('报价区间').size()
print(grouped)
arr = grouped.values
print(arr)
#已分理出数组元素，下面进行画图操作

rcParams['font.sans-serif'] = ['SimHei']
plt.figure(400)
plt.title('报价分布图（单位：万元）')
lables = ['0-10','10-20','20-30','30-50','50-100','100万以上']
plt.legend(loc='best') 
plt.pie(arr, labels=labels, autopct='%1.1f%%',explode=[0.1,0.1,0.1,0.1,0.1,0.1])
plt.savefig('pie.png')
plt.show()


'''
print('---------- 绘制圆饼图 ----------')
y2=np.random.randint(0,100,6)

plt.figure(300)
plt.pie(y2,explode=[0.1,0.1,0.1,0.1,0.1,0.1])
plt.savefig('pie.png')
plt.show()'''
