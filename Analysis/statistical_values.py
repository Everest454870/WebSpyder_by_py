
# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('car_message.csv',encoding='utf-8')
df_price = df.loc[:,'报价']
df_price_min = df_price.min()
df_price_max = df_price.max()
df_price_mean = df_price.mean()
df_price_median = df_price.median()
print("最小报价",df_price_min)
print("最大报价",df_price_max)
print("报价均值",df_price_mean)
print("报价中位数",df_price_median)

selected_rows_min = df[df['报价'] == df_price_min]
Selected_rows_min = selected_rows_min.to_string(index=False,header=False)
print(f"最小报价对应的车型为：\n{Selected_rows_min}")

selected_rows_max = df[df['报价'] == df_price_max]
Selected_rows_max = selected_rows_max.to_string(index=False,header=False)
print(f"最高报价对应的车型为：\n{Selected_rows_max}")


