import pandas as pd

def load_data():
    df = pd.read_csv("data/Indianclimate.csv")
    
    print("\nFirst 5 rows of dataset:\n")
    print(df.head())

    print("\nDataset Structure:\n")
    print(df.info())
    print("-"*60)
    return df
