# Medicare Star Ratings Analysis for Part C and D Plans

## Overview

This project focuses on analyzing Medicare star ratings for Part C (Medicare Advantage) and Part D (Prescription Drug Plans) using Python. The analysis aims to uncover insights related to plan quality, measure performance, geographic variations, and trends. The project also showcases various data science techniques such as data cleaning, exploratory data analysis (EDA), and predictive modeling to help understand what factors contribute to the overall ratings of these healthcare plans.

## Dataset

The dataset used in this analysis was obtained from the Centers for Medicare & Medicaid Services (CMS). The data includes star ratings, contract information, plan details, and ratings for individual measures that determine the overall score. You can download the data from the CMS Data Portal.

## Project Structure

**data/**: Contains the original and processed datasets.

**notebooks/**: Jupyter notebooks for analysis and modeling.

**scripts/**: Python scripts used for data cleaning, exploratory analysis, and modeling.

**README.md**: This file, explaining the project and how to get started.

## Steps to Run the Analysis

### Install Dependencies:
The analysis uses several Python libraries such as **pandas, matplotlib, seaborn,** and **scikit-learn**. You can install all the dependencies using the command:

![Fig 1](https://github.com/mjada76/Work_Projects/blob/Visualization/Figure_1.png)

### Load the Data:
Load the Medicare star ratings dataset by either placing the data file in the **data/** directory or providing the path within the notebook. The analysis notebooks will guide you on the structure of the data.

### Run the Jupyter Notebook:
The main analysis is performed in the Jupyter notebook file (`2024_CMS_Star_Rating.ipynb`). You can run this notebook step-by-step to see the data cleaning, visualization, and modeling procedures.

## Key Features of the Analysis

### Exploratory Data Analysis (EDA):
We use **pandas, matplotlib**, and **seaborn** to explore the distribution of overall star ratings and individual measures. Visualizations such as bar plots and heatmaps help provide insights into what measures impact ratings.

### Comparing Plan Types:
We differentiate between Part C and Part D plans, analyzing the performance of each type. This includes comparing average ratings and identifying patterns for improvement.

### Measure Correlation Analysis:
The analysis includes examining the correlation between individual measures and the overall star rating, providing insights into which metrics significantly contribute to plan quality.

### Predictive Modeling (Optional):
Using **scikit-learn**, we create a simple Random Forest model to predict star ratings based on individual measure ratings. This helps in understanding the relative importance of each measure in determining the overall rating.

## Visualization Examples

### The visualizations include:

Distribution of Star Ratings: A bar plot showing the frequency of plans with different ratings, which helps in understanding the quality spread across plans.

State-wise Performance: A bar chart that shows the average star rating by state, highlighting regional variations in plan quality.

## Getting Started
To get started, clone this repository and install the necessary Python libraries:

![Code Snip](....\Visualization\Snippet.png)

Once the dependencies are installed, you can explore the data and run the analyses using the Jupyter notebooks available in the __notebooks/__

## Future Enhancements

Improved Predictive Models: Adding more advanced models, such as Gradient Boosting or XGBoost, to improve prediction accuracy.

Dashboard Visualization: Creating an interactive dashboard using tools like Plotly Dash or Tableau for easier visualization of insights.

Geospatial Analysis: Adding geospatial analysis to understand how Medicare plan quality varies across different regions in more detail.


