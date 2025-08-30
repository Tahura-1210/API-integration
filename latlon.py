import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')  # Load a sample dataset

# Create a scatter plot
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')

# Add title
plt.title('Scatter Plot of Tips vs. Total Bill')

# Show the plot
plt.show()