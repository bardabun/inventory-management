import pandas as pd
import numpy as np


d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}




df = pd.DataFrame(d)
df['three'] = pd.Series([9, 12, 13], index=['a', 'b', 'd'])
df['mul : one + two'] = df['one'] * df['two'] + df['three']
df.to_excel(r'C:\Users\Tomer\Desktop\myTester\Tempt123.xlsx')
df.to_csv(r'C:\Users\Tomer\Desktop\myTester\Tempt123.csv')
df2 = pd.DataFrame(d)
print(df2.describe())
print("Finished")
