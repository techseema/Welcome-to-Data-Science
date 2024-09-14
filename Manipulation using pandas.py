import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Filter data for people aged 30 or older
filtered_df = df[df['Age'] >= 30]

# Calculate the average age
average_age = df['Age'].mean()

# Group data by city and calculate the count of each city
city_counts = df['City'].value_counts()

print("Filtered Data:")
print(filtered_df)

print("Average Age:", average_age)

print("City Counts:")
print(city_counts)