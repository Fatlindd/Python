import pandas as pd


def read_csv(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as fnf_err:
        print(f"File not found: {fnf_err}")
    except pd.errors.EmptyDataError as ede_err:
        print(f"Empty data error: {ede_err}")
    except pd.errors.ParserError as parse_err:
        print(f"Parser error: {parse_err}")
    except Exception as e:
        print(f"An error occurred: {e}")


def perform_analysis(df):
    if df is not None:
        # Calculate basic statistics
        mean_value = df['value'].mean()
        median_value = df['value'].median()
        mode_value = df['value'].mode()[0]

        # Filter data: Get rows where the value is greater than the mean
        filtered_df = df[df['value'] > mean_value]

        # Sort data: Sort by value in descending order
        sorted_df = filtered_df.sort_values(by='value', ascending=False)

        # Group and aggregate data: Group by category and calculate the sum of values
        grouped_df = df.groupby('category')['value'].sum().reset_index()

        return {
            "mean": mean_value,
            "median": median_value,
            "mode": mode_value,
            "filtered": filtered_df,
            "sorted": sorted_df,
            "grouped": grouped_df
        }
    else:
        print("No DataFrame to analyze")
        return None


def output_results(results, output_file_path):
    if results:
        print(f"Mean Value: {results['mean']}")
        print(f"Median Value: {results['median']}")
        print(f"Mode Value: {results['mode']}")

        print("\nFiltered DataFrame:")
        print(results['filtered'])

        print("\nSorted DataFrame:")
        print(results['sorted'])

        print("\nGrouped DataFrame:")
        print(results['grouped'])

        # Save the grouped DataFrame to a new CSV file
        results['grouped'].to_csv(output_file_path, index=False)
        print(f"\nGrouped DataFrame saved to {output_file_path}")
    else:
        print("No results to output")


def main():
    input_file_path = 'data.csv'
    output_file_path = 'grouped_data.csv'

    df = read_csv(input_file_path)
    results = perform_analysis(df)
    output_results(results, output_file_path)


if __name__ == "__main__":
    main()
