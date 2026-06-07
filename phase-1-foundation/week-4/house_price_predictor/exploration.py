import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Housing.csv")
print("data:\n", df.head())
print("description:\n", df.describe())
print("info:\n", df.info())
print("shape:\n", df.shape)
print("columns:\n", df.columns)
print("dtypes:\n", df.dtypes)
print("isnull:\n", df.isnull().sum())

categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
for col in categorical_columns:
    print(f"unique values of {col}:\n", df[col].unique())

numerical_columns = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
print(df[numerical_columns].describe().loc[['min', 'max']])