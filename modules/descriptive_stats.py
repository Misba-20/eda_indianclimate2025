import pandas as pd

def descriptive_statistics(cleaned_data):
    numeric_cols = cleaned_data.select_dtypes(include='number').columns
    print("\n----- Descriptive Statistics -----\n")
    
    for col in numeric_cols:
        print(f"Column: {col}")
        print(f"Mean: {cleaned_data[col].mean():.2f}")
        print(f"Median: {cleaned_data[col].median():.2f}")
        print(f"Mode: {cleaned_data[col].mode()[0]}")
        print(f"Standard Deviation: {cleaned_data[col].std():.2f}")
        print(f"Minimum: {cleaned_data[col].min()}")
        print(f"Maximum: {cleaned_data[col].max()}")
        print("-" * 40)
