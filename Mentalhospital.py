import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TextVectorization, Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.optimizers import Adam

# Step 1: Load the CSV file with statements and associated illnesses
def load_csv(file_path="new.csv"):
    try:
        # Load the CSV file into a DataFrame (without headers)
        df = pd.read_csv(file_path, header=None)
        # Assume the first column is 'Statement' and the second is 'Status'
        df.columns = ['Statement', 'Status']
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# Step 2: Preprocess and encode the labels
def preprocess_data(df):
    # Vectorize the text data using a TextVectorization layer
    vectorizer = TextVectorization(max_tokens=10000, output_mode='int', output_sequence_length=100)
    vectorizer.adapt(df['Statement'].values)
    
    # Encode the illness labels
    label_encoder = LabelEncoder()
    df['Status'] = label_encoder.fit_transform(df['Status'])
    
    return df['Statement'].values, df['Status'].values, vectorizer, label_encoder

# Step 3: Build the model
def build_model(vectorizer, num_classes):
    model = Sequential([
        vectorizer,
        Embedding(input_dim=10000, output_dim=64, input_length=100),
        GlobalAveragePooling1D(),
        Dense(64, activation='relu'),
        Dense(num_classes, activation='softmax')  # Use softmax for multi-class classification
    ])
    
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Step 4: Train the model
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)
    return model

# Step 5: Handle predictions and interact with the user
def main():
    # Load data and preprocess
    file_path = "new.csv"
    df = load_csv(file_path)
    
    if df is None:
        return

    X_train, y_train, vectorizer, label_encoder = preprocess_data(df)

    # Build and train the model
    num_classes = len(label_encoder.classes_)
    print(f"Detected {num_classes} unique classes: {label_encoder.classes_}")
    
    print("Training the model...")
    model = build_model(vectorizer, num_classes)
    model = train_model(model, X_train, y_train)
    
    print("Training complete. You can now input statements for prediction.")
    print("This AI tool is for informational purposes only and does not provide medical advice, diagnosis, or therapy. No therapist-client relationship is established, and it is not a substitute for professional care. If you're in crisis, please contact a licensed professional or emergency services immediately.")
    while True:
        input_text = input("\nEnter a statement (or type 'exit' to quit): ")
        if input_text.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Ensure the input is in the correct format for vectorization
            input_vectorized = tf.constant([input_text])  # Wrap input in a list
            prediction = model.predict(input_vectorized)
            
            # Decode the prediction
            predicted_label_index = np.argmax(prediction)
            predicted_label = label_encoder.inverse_transform([predicted_label_index])
            print(f"Predicted Illness: {predicted_label[0]}")
        except Exception as e:
            print(f"Error during prediction: {e}")

if __name__ == "__main__":
    main()

