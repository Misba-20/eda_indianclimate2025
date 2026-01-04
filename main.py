from modules.import_data import load_data
from modules.handling_missing_value import handle_missing_values
from modules.data_transformation import normalize_data, standardize_data
from modules.descriptive_stats import descriptive_statistics
from modules.basic_visualizations import basic_visualizations
from modules.advanced_visualizations import advanced_visualizations
from modules.probability_analysis import probability_analysis
from modules.kmeans_modeling import kmeans_clustering_model
from modules.dashboard import create_dashboard

if __name__ == "__main__":

    # Load dataset
    data = load_data()

    # Handle missing values
    cleaned_data = handle_missing_values(data)
    cleaned_data.to_csv('cleaned_dataset.csv', index=False)
    print("\nCleaned dataset saved as 'cleaned_dataset.csv'")

    # Data transformation
    normalized_df = normalize_data(cleaned_data)
    standardized_df = standardize_data(cleaned_data)

    # Analysis
    descriptive_statistics(cleaned_data)
    basic_visualizations(cleaned_data)
    advanced_visualizations(cleaned_data)
    probability_analysis(cleaned_data)

    # K-Means Modeling
    kmeans_clustering_model(cleaned_data)

    # Dashboard
    app = create_dashboard(cleaned_data)
    app.run(debug=True, use_reloader=False)
