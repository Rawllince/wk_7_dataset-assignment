# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import mean

# Column names from adult.names
columns = [
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
]

# Load dataset
try:
    df = pd.read_csv(r"D:\Desktop\wk-7-python\adult.csv", header=None, names=columns, sep=",", skipinitialspace=True)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset file not found. Please check the file path.")
    df = None

if df is not None:
    # Inspect the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Check structure of dataset
    print("\nDataset Info:")
    print(df.info())

    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean dataset by dropping or filling missing values
    df = df.dropna()
    print("\nAfter cleaning, missing values:")
    print(df.isnull().sum())

    # Task 2: Basic Data Analysis
    print("\nDescriptive Statistics:")
    print(df.describe())

    # Example grouping: average age per education level
    grouped = df.groupby("education")["age"].mean().sort_values(ascending=False)
    print("\nAverage Age per Education Level:")
    print(grouped)

    print("\nInteresting Finding:")
    print("Higher education levels (like Doctorate, Masters) tend to have higher average age compared to lower education levels.")

    # Task 3: Data Visualization
    sns.set(style="whitegrid")

    # 1. Line chart (Age distribution by index, first 100 records)
    plt.figure(figsize=(10,6))
    plt.plot(df.index[:100], df["age"].head(100), marker="o")
    plt.title("Line Chart: Age Trend (First 100 Records)")
    plt.xlabel("Index")
    plt.ylabel("Age")
    plt.show()

    # 2. Bar chart (Average hours-per-week by education)
    plt.figure(figsize=(12,6))
    sns.barplot(x="education", y="hours-per-week", data=df, estimator=mean)
    plt.title("Bar Chart: Average Weekly Working Hours per Education Level")
    plt.xticks(rotation=45)
    plt.show()

    # 3. Histogram (Age distribution)
    plt.figure(figsize=(10,6))
    sns.histplot(df["age"], bins=20, kde=True)
    plt.title("Histogram: Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter plot (Age vs. Hours-per-week)
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="age", y="hours-per-week", hue="sex", data=df, alpha=0.6)
    plt.title("Scatter Plot: Age vs. Hours-per-week (Colored by Sex)")
    plt.xlabel("Age")
    plt.ylabel("Hours per Week")
    plt.legend(title="Sex")
    plt.show()