import matplotlib.pyplot as plt
import seaborn as sns

def probability_analysis(cleaned_data):

    numeric_cols = cleaned_data.select_dtypes(include='number').columns[:2]

    print("\n----- Probability Analysis -----")

    for col in numeric_cols:
        print(f"\nColumn: {col}")

        # Range and Variance
        data_range = cleaned_data[col].max() - cleaned_data[col].min()
        variance = cleaned_data[col].var()

        print(f"Range: {data_range}")
        print(f"Variance: {variance:.2f}")

        # Histogram after analysis
        plt.figure()
        sns.histplot(cleaned_data[col], kde=True)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()
