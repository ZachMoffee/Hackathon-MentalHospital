import pandas as pd

def capitalize_first_word(text):
    if not isinstance(text, str) or not text.strip():
        return text
    words = text.strip().strip('"').split()
    if not words:
        return text
    words[0] = words[0].capitalize()
    return ' '.join(words)

def capitalize_first_words_in_place(filename="new.csv"):
    df = pd.read_csv(filename)

    # Apply capitalization function to both 'statement' and 'status' columns
    df['statement'] = df['statement'].astype(str).apply(capitalize_first_word)
    df['status'] = df['status'].astype(str).apply(capitalize_first_word)

    # Save the modified DataFrame back to the same file
    df.to_csv(filename, index=False)
    print(f"✅ Capitalized first word in both columns and updated '{filename}' in place.")

if __name__ == "__main__":
    capitalize_first_words_in_place()
