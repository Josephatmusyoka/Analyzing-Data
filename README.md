# Data Analysis with Pandas and Visualization using Matplotlib

## Objective:
The goal of this assignment is to perform data analysis using the **Pandas** library and create visualizations using the **Matplotlib** library in Python. The analysis involves loading a dataset, exploring the data, performing basic statistical analysis, and creating visualizations to gain insights from the data.

## Dataset:
The dataset used in this assignment is the **Iris Dataset**. It is a well-known dataset used for classification and clustering tasks, which contains measurements of 150 iris flowers from three different species.

## Tasks:

### Task 1: Load and Explore the Dataset
1. **Load the dataset**: The dataset is loaded using **Seaborn** (`sns.load_dataset('iris')`).
2. **Inspect the dataset**: The first few rows of the dataset are displayed using `iris.head()`.
3. **Explore the structure**: We explore the dataset to check for missing values and view data types using `iris.info()` and `iris.isnull().sum()`.

### Task 2: Basic Data Analysis
1. **Statistical Summary**: We generate basic statistical summaries of the numerical columns using `iris.describe()`.
2. **Group by Species**: The dataset is grouped by species, and the average of numerical columns is computed for each species using `iris.groupby('species').mean()`.

### Task 3: Data Visualization
We create the following visualizations using **Matplotlib**:

1. **Bar Chart**: A bar chart displaying the average petal length by species.
2. **Histogram**: A histogram to show the distribution of sepal length.
3. **Scatter Plot**: A scatter plot showing the relationship between sepal length and petal length.

## Requirements:
Before running the script, ensure that you have the following Python libraries installed:

- **Pandas**: for data manipulation and analysis.
- **Seaborn**: for loading the dataset.
- **Matplotlib**: for plotting visualizations.

You can install these libraries using pip:

```bash
pip install pandas seaborn matplotlib
