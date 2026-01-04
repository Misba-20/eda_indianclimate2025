import matplotlib.pyplot as plt

def basic_visualizations(df):
    numeric_cols = df.select_dtypes(include='number').columns[:2]
    print("----- Creating Basic Visualizations -----\n")
    
    # Line Plot for each numeric column
    for col in numeric_cols:
        plt.figure(figsize=(8,4))
        plt.plot(df[col], marker='o', linestyle='-', color='skyblue')
        plt.title(f'Line Plot of {col}')
        plt.xlabel('Index')
        plt.ylabel(col)
        plt.grid(True)
        plt.show()
    
    # Histogram for each numeric column
    for col in numeric_cols:
        plt.figure(figsize=(8,4))
        plt.hist(df[col], bins=20, color='g', edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.grid(axis='y')
        plt.show()
    
    # Bar Chart for first 10 rows of each numeric column
    for col in numeric_cols:
        plt.figure(figsize=(8,4))
        plt.bar(df.index[:10], df[col][:10], color='lavender', edgecolor='black')
        plt.title(f'Bar Chart of {col} (first 10 rows)')
        plt.xlabel('Index')
        plt.ylabel(col)
        plt.show()
    print("Created successfully")
    return None
