import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load a built-in dataset
iris = sns.load_dataset('iris')

# Create a 3D figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 3D scatter plot
scatter = ax.scatter(iris['sepal_length'], iris['sepal_width'], iris['petal_length'], c=iris['species'])

# Set labels and title
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
plt.title('Iris 3D Scatter Plot')

# Add a legend
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower right", title="Species")
ax.add_artist(legend1)

# Show the plot
plt.show()