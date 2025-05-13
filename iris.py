# Iris Dataset Analysis
# This notebook demonstrates loading, exploring, analyzing, and visualizing the Iris dataset using pandas and matplotlib.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# %% 
# ## Task 1: Load and Explore the Dataset
# Load the dataset
try:
    iris = load_iris()
    iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                         columns=iris['feature_names'] + ['target'])
    iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    print("Dataset loaded successfully!")
    print("\nFirst 5 rows:")
    display(iris_df.head())
    
except Exception as e:
    print(f"Error loading dataset: {e}")

# %%
# Explore dataset structure
print("\nDataset Info:")
iris_df.info()

# %%
# Check for missing values
print("\nMissing values per column:")
print(iris_df.isnull().sum())

# Since there are no missing values in this dataset, no cleaning is needed
# %% 
# ## Task 2: Basic Data Analysis
# Basic statistics
print("\nBasic statistics for numerical columns:")
display(iris_df.describe())

# %%
# Group by species and calculate means
print("\nMean measurements by species:")
species_means = iris_df.groupby('species').mean()
display(species_means)

# %%
# Interesting findings observation
print("\nKey Observations:")
print("1. Setosa has significantly smaller petal length and width compared to other species")
print("2. Virginica has the largest sepal length on average")
print("3. All species have similar sepal widths, with versicolor being slightly narrower")

# %% 
# ## Task 3: Data Visualization
# Set style for better looking plots
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# %% 
# ### Visualization 1: Line Chart (Trend of Sepal Length by Index)
# Line chart showing sepal length by index (simulating trend over time)
plt.plot(iris_df['sepal length (cm)'])
plt.title('Sepal Length Trend (by Sample Index)')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# %% 
# ### Visualization 2: Bar Chart (Average Measurements by Species)
# Bar chart of average measurements by species
species_means.plot(kind='bar')
plt.title('Average Measurements by Iris Species')
plt.ylabel('Centimeters')
plt.xticks(rotation=0)
plt.legend(title='Measurement')
plt.show()

# %% 
# ### Visualization 3: Histogram (Distribution of Petal Length)
# Histogram of petal length
plt.hist(iris_df['petal length (cm)'], bins=15, edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# %% 
# ### Visualization 4: Scatter Plot (Sepal Length vs Petal Length)
# Scatter plot of sepal length vs petal length
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
plt.scatter(iris_df['sepal length (cm)'], iris_df['petal length (cm)'],
            c=iris_df['species'].map(colors))
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

# Create legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Setosa',
                             markerfacecolor='red', markersize=8),
                  plt.Line2D([0], [0], marker='o', color='w', label='Versicolor',
                             markerfacecolor='green', markersize=8),
                  plt.Line2D([0], [0], marker='o', color='w', label='Virginica',
                             markerfacecolor='blue', markersize=8)]
plt.legend(handles=legend_elements)
plt.show()

# %% 
# Pair plot showing all variable relationships
sns.pairplot(iris_df, hue='species')
plt.suptitle('Pairwise Relationships in Iris Dataset', y=1.02)
plt.show()

# %% 
# ## Summary of Findings
# 
# 1. **Species Differences**: The three iris species have distinct measurements, especially in petal dimensions.
# 2. **Setosa Characteristics**: Iris setosa has notably smaller petals than the other species.
# 3. **Virginica Size**: Iris virginica tends to be the largest in both sepal and petal measurements.
# 4. **Strong Correlation**: There appears to be a strong positive correlation between petal length and width.
# 5. **Distinct Groups**: The scatter plots show clear separation between species, especially setosa from the other two.