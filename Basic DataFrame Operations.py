import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Access a column
print(df['Name'])

# Access a row
print(df.iloc[1])  # Second row (index 1)

# Filter rows
print(df[df['Age'] > 30])

# Add a new column
df['Salary'] = [70000, 80000, 90000]
print(df)

# Describe the DataFrame (summary statistics)
print(df.describe())
