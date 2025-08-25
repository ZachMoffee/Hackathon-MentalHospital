import pandas as pd

def lowercase_all_text(filename="new.csv"):
    df = pd.read_csv(filename)

    # Convert all characters in both columns to lowercase
    df['statement'] = df['statement'].astype(str).str.lower()
    df['status'] = df['status'].astype(str).str.lower()

    # Save the modified file in place
    df.to_csv(filename, index=False)
    print(f"✅ All text converted to lowercase and saved back to '{filename}'.")

if __name__ == "__main__":
    lowercase_all_text()
