import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def normalize_data(cleaned_data):
    """
    Apply Min-Max normalization to numeric columns of the DataFrame.
    Returns a new DataFrame with normalized values.
    """
    numeric_cols = cleaned_data.select_dtypes(include='number').columns
    scaler = MinMaxScaler()
    normalized_cleaned_data = pd.DataFrame(scaler.fit_transform(cleaned_data[numeric_cols]), columns=numeric_cols)
    
    print("\nNormalized Data (Min-Max scaling):")
    print(normalized_cleaned_data.head())
    return normalized_cleaned_data

def standardize_data(cleaned_data):
    """
    Apply Z-score standardization to numeric columns of the DataFrame.
    Returns a new DataFrame with standardized values.
    """
    numeric_cols = cleaned_data.select_dtypes(include='number').columns
    scaler = StandardScaler()
    standardized_cleaned_data = pd.DataFrame(scaler.fit_transform(cleaned_data[numeric_cols]), columns=numeric_cols)
    
    print("\nStandardized Data (Z-score scaling):")
    print(standardized_cleaned_data.head())
    return standardized_cleaned_data
