import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Merge DataFrames on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)
