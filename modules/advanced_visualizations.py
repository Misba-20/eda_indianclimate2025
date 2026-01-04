import seaborn as sns
import matplotlib.pyplot as plt

def advanced_visualizations(df):
    numeric_cols = df.select_dtypes(include='number').columns
    print("----- Advanced Visualizations -----\n")

    # 1. Pair Plot
    sns.pairplot(df[numeric_cols])
    plt.suptitle("Pair Plot of Numeric Climate Features", y=1.02)
    plt.show()

    # 2. Correlation Heatmap
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(10,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap of Climate Features")
    plt.xlabel("Features")
    plt.ylabel("Features")
    plt.show()

    # 3. Covariance Heatmap
    cov = df[numeric_cols].cov()
    plt.figure(figsize=(10,6))
    sns.heatmap(cov, annot=True, cmap='viridis', fmt=".2f")
    plt.title("Covariance Heatmap of Climate Features")
    plt.xlabel("Features")
    plt.ylabel("Features")
    plt.show()


    print("Created successfully")
    return None
