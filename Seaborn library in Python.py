import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in dataset
tips = sns.load_dataset('tips')

# Create a scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips)

# Show the plot
plt.show()