# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# List of file paths to CSV files to be processed
file_paths = [
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_HEDIS_Under_500_Display_11_13_2023.csv',
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_HPMS_Display_Measures.csv',
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_HPMS_Display_Measures_12_14_2023.csv',
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_MAPD_Part D_Measures.csv',
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_Part C_Measures.csv',
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_Part C_Star_Averages.csv',
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_Part D_Measures.csv',
    r'C:\Users\m_jad\OneDrive\Desktop\The Work Folder\Alight\Analysis\2024_Part D_Star_Averages.csv'
]

# Process each file
for file_path in file_paths:
    print(f"Processing file: {file_path}")
    
    try:
        # Load the data from the CSV file into a pandas DataFrame
        data = pd.read_csv(file_path, encoding='ISO-8859-1')
        
        # Preview the first few rows of the dataset
        print(data.head())
        
        # Basic information about the dataset
        print(data.info())
        
        # Display summary statistics
        print(data.describe())
        
        # Check for missing values
        print(data.isnull().sum())
        
        # Check the column names
        print("Column names:", data.columns)
        
        # Clean up column names (strip whitespace)
        data.columns = data.columns.str.strip()
        
        # List of star rating columns to check
        star_rating_columns = ['2024 Star Average', '2024 MAPD Star Average', '2024 PDP Star Average']

        # Remove columns that are entirely unnamed
        data_cleaned = data.dropna(axis=1, how='all') 
        
        # Plot the distribution of each star rating column if it exists
        for column in star_rating_columns:
            if column in data.columns:
                plt.figure(figsize=(10, 6))
                sns.countplot(x=column, data=data, palette="Blues")
                plt.title(f'Distribution of {column} for {file_path}')
                plt.show()
            else:
                print(f"Column '{column}' not found in the data.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Using a Random Forest Regressor to predict Medicare Star Ratings
# Ensure the correct column name is used for the target
if '2024 Star Average' in data.columns:
    # Select features and target
    measures = ['Feature1', 'Feature2', 'Feature3']  # Replace with actual feature column names
    features = data[measures]
    target = data['2024 Star Average']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

    # Train the model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Make predictions and evaluate
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f'RMSE: {rmse}')