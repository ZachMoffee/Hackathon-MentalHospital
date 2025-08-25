import pandas as pd

def remove_string_nan_rows(input_file="new.csv", output_file="cleaned_output.csv"):
    # Load CSV
    df = pd.read_csv(input_file)

    # Convert columns to lowercase string and strip whitespace
    df['statement'] = df['statement'].astype(str).str.strip().str.lower()
    df['status'] = df['status'].astype(str).str.strip().str.lower()

    # Remove rows where either column is exactly "nan"
    df_cleaned = df[(df['statement'] != 'nan') & (df['status'] != 'nan')]

    # Save cleaned output
    df_cleaned.to_csv(output_file, index=False)
    print(f"✅ All rows with 'nan' in either column removed. Saved to '{output_file}'.")

if __name__ == "__main__":
    remove_string_nan_rows()