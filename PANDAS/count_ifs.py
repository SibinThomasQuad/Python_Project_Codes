import pandas as pd

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 32, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago']}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Define your conditions
condition1 = (df['Age'] > 30)  # Example: Age greater than 30
condition2 = (df['City'] == 'New York')  # Example: City is 'New York'

# Apply the conditions and use 'sum' to count the matches
count = (condition1 & condition2).sum()

print(f'Count of records meeting the conditions: {count}')
