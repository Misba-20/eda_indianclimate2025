import pandas as pd

def handle_missing_values(df):
    # ---------- Handle Missing Values ----------
    print("Missing values (isnull) before cleaning:")
    print(df.isnull().sum())
    print("\nNon-missing values (notnull) before cleaning:")
    print(df.notnull().sum())

    # Fill numeric columns with mean
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    print("\nMissing values after filling numeric columns with mean:")
    print(df.isnull().sum())

    # Remove duplicate rows
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"\nRemoved {before - after} duplicate rows, if any.")

    # Keep only complete rows
    df = df[df.notnull().all(axis=1)]

    print("\nMissing values after cleaning and removing duplicates:")
    print(df.isnull().sum())
    print("\nNon-missing values after cleaning and removing duplicates:")
    print(df.notnull().sum())

    # ---------- Identify and Handle Outliers (IQR Method) ----------
    for col in numeric_cols:
        print(f"\nHandling outliers in column: {col}")

        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        print(f"Number of outliers in {col}: {outliers.shape[0]}")

        # Remove outliers
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

        print(f"After removing outliers, {col} stats:")
        print(df[col].describe())

    return df
