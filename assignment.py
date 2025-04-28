# assignment.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset using seaborn
    iris = sns.load_dataset('iris')
    print("Dataset Loaded Successfully!")
    
    # Display the first few rows to inspect the dataset
    print("\nFirst few rows of the dataset:")
    print(iris.head())

    # Explore the structure of the dataset
    print("\nDataset Information:")
    print(iris.info())  # Data types and non-null counts
    print("\nMissing Values in the dataset:")
    print(iris.isnull().sum())  # Check for missing values

    # Task 2: Basic Data Analysis
    print("\nBasic Statistical Summary of Numerical Columns:")
    print(iris.describe())  # Basic statistics for numerical columns

    # Group by 'species' and calculate the mean of numerical columns
    print("\nAverage numerical values per species:")
    species_means = iris.groupby('species').mean()
    print(species_means)

    # Task 3: Data Visualization
    # 1. Bar Chart: Average Petal Length by Species
    plt.figure(figsize=(8, 6))
    iris.groupby('species')['petal_length'].mean().plot(kind='bar', color='lightblue')
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length')
    plt.xticks(rotation=45)
    plt.show()

    # 2. Histogram: Distribution of Sepal Length
    plt.figure(figsize=(8, 6))
    plt.hist(iris['sepal_length'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Frequency')
    plt.show()

    # 3. Scatter Plot: Sepal Length vs Petal Length
    plt.figure(figsize=(8, 6))
    plt.scatter(iris['sepal_length'], iris['petal_length'], color='green', edgecolors='black')
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.show()

except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
