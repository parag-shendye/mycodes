import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from sklearn import preprocessing

df =pd.read_excel("titanic.xls")

df.drop(['name','body'],axis=1,inplace=True)
df.fillna(0,inplace=True)
print(df.isnull().sum())
print(df.columns)


def handle_non_numeric_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def conver_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype!= np.int64 and df[column].dtype!= np.float64:
            column_contents = df[column].values.tolist()
            unique_elemts = set(column_contents)
            x=0
            for unique in unique_elemts:
                if unique not in text_digit_vals:
                    text_digit_vals[unique]=x
                    x+=1

            df[column]=list(map(conver_to_int,df[column]))

    return df

df = handle_non_numeric_data(df)
print(df.head())



