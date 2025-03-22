import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, np.nan, 40],
    'City': ['New York', np.nan, 'Chicago', 'Los Angeles']
}

df = pd.DataFrame(data)

# Check for missing values
print(df.isnull())

# Drop rows with missing values
df_cleaned = df.dropna()
print(df_cleaned)

# Fill missing values with a default value
df_filled = df.fillna({'Age': 0, 'City': 'Unknown'})
print(df_filled)
