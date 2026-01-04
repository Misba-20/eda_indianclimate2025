import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def kmeans_clustering_model(cleaned_data):
    print("\n----- K-Means Clustering -----")

    # Select numeric columns only
    numeric_df = cleaned_data.select_dtypes(include='number')

    # Standardize data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)

    # Apply KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    cleaned_data['Cluster'] = kmeans.fit_predict(scaled_data)

    print("\nCluster Count:")
    print(cleaned_data['Cluster'].value_counts())

    # Scatter Plot
    plt.figure()
    plt.scatter(numeric_df.iloc[:,0], numeric_df.iloc[:,1], c=cleaned_data['Cluster'])
    plt.xlabel(numeric_df.columns[0])
    plt.ylabel(numeric_df.columns[1])
    plt.title("K-Means Clustering Scatter Plot")
    plt.show()

    # Pair Plot
    sns.pairplot(cleaned_data, hue='Cluster')
    plt.show()

    # Interpretation
    print("\n--- Cluster Interpretation ---")
    print(cleaned_data.groupby('Cluster').mean(numeric_only=True))
