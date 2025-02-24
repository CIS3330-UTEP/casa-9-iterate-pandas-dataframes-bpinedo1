import pandas as pd

filename= "./big-mac-full-index.csv"
df= pd.read_csv(filename)

print(df)

for index, row in df.iterrows():
    print(f"Index: {index}") 
