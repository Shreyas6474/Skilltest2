# -*- coding: utf-8 -*-
"""Skill test2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12zQCdQMaE92fS936IXCUMOa42-tez8CR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/content/AMC.csv")

data.describe()

data.head()

data.tail()

data.info()

data.nunique()

data.isnull().sum()

data.isnull().sum()/(len(data))

data = data.drop(['Close'], axis=1)
data.info()

from datetime import date
current_year = date.today().year
data['Date'] = current_year - data['Open']
data.head()

data.describe().T

print(data.Date.unique())
print(data.Open.unique())

cat_cols = data.select_dtypes(include=['object']).columns
num_cols = data.select_dtypes(include=np.number).columns.tolist()

print("Categorical variables:")
print(cat_cols)
print("Numerical variables:")
print(num_cols)

data1 = data.dropna()
print(data1)
data.info

data2 = data.dropna(axis=1)
print(data2)
data.info

data3 = data.fillna(data.mean())
print(data3)
data.info

import pandas as pd
df=pd.read_csv("/content/AMC.csv")
z_scores=(df-df.mean())/df.std()
outliers=df[abs(z_scores)>3]
print("univariate outliers:",outliers)

