import pandas as pd

def clean_status_column(df, column_name='status'):
    # Ensure all values are strings, strip whitespace
    df[column_name] = df[column_name].astype(str).str.strip()
    return df

def main():
    input_file = "new.csv"
    output_file = "filtered_output.csv"

    # Load and clean the CSV
    df = pd.read_csv(input_file)
    df = clean_status_column(df, 'status')

    # Get sorted unique values in 'status'
    unique_statuses = sorted(df['status'].dropna().unique())

    print("Review each STATUS and decide whether to delete rows with it:\n")

    for status in unique_statuses:
        if status.lower() == 'nan' or status.strip() == '':
            continue  # skip invalid/blank
        while True:
            choice = input(f"Delete rows with STATUS '{status}'? (Y/N): ").strip().upper()
            if choice == 'Y':
                df = df[df['status'] != status]  # DELETE immediately
                print(f"✅ Deleted all rows with status '{status}'")
                break
            elif choice == 'N':
                break
            else:
                print("Invalid input. Enter Y or N.")

    # Save filtered output
    df.to_csv(output_file, index=False)
    print(f"\n✅ Done! Filtered data saved to '{output_file}'.")

if __name__ == "__main__":
    main()
