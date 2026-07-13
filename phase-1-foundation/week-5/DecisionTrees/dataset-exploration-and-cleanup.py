import pandas as pd
import os

print(os.getcwd())

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'breast-cancer-data.csv') 

df = pd.read_csv(file_path)
print(df.head())
# print(df.describe())
# print(df.info())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.isnull().sum())

print("unique values of 'diagnosis':\n", df['diagnosis'].unique())
print("unique values of id:", df['id'].nunique(), " & df len:", len(df)) # 569 == 569 i.e. all are unique its just a index column

# dropping unknown and id column
df = df.drop(columns=['id', 'Unnamed: 32'])

print(df.head())

# Encoding the diagnosis column
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df['diagnosis'].value_counts())

df.to_csv('breast-cancer-data-cleaned.csv', index=False)