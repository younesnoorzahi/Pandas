import pandas as pd

# Create a DataFrame
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago'],
    'Sales': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

# Group by 'City' and calculate the sum of 'Sales'
grouped = df.groupby('City').sum()
print(grouped)
