import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Load the dataset
data = pd.read_csv("names_to_train.csv", header=None)
df = pd.DataFrame(data)

# Prepare the data
names = data[0].values
labels = data[1].values
names = names.tolist()
labels = labels.tolist()

# Convert labels to numerical values
label_to_int = {"male": 0, "female": 1}
label_ints = [label_to_int[label] for label in labels]

# Split the dataset into training and validation sets
train_names, val_names, train_labels, val_labels = train_test_split(names, label_ints, test_size=0.2, random_state=42)

# Convert labels and encodings to NumPy arrays with appropriate data types
train_labels = np.array(train_labels, dtype=np.int32)
val_labels = np.array(val_labels, dtype=np.int32)

# Load the pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Tokenize the input names
train_encodings = tokenizer(train_names, truncation=True, padding=True)
val_encodings = tokenizer(val_names, truncation=True, padding=True)

train_encodings = {
    'input_ids': np.array(train_encodings['input_ids'], dtype=np.int32),
    'attention_mask': np.array(train_encodings['attention_mask'], dtype=np.int32),
    'token_type_ids': np.array(train_encodings['token_type_ids'], dtype=np.int32)
}

val_encodings = {
    'input_ids': np.array(val_encodings['input_ids'], dtype=np.int32),
    'attention_mask': np.array(val_encodings['attention_mask'], dtype=np.int32),
    'token_type_ids': np.array(val_encodings['token_type_ids'], dtype=np.int32)
}

# Create TensorFlow datasets
train_dataset = tf.data.Dataset.from_tensor_slices((
    dict(train_encodings),
    train_labels
)).batch(16)

val_dataset = tf.data.Dataset.from_tensor_slices((
    dict(val_encodings),
    val_labels
)).batch(16)

# Fine-tune the BERT model
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-5)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metric = tf.keras.metrics.SparseCategoricalAccuracy('accuracy')

model.compile(optimizer=optimizer, loss=loss, metrics=[metric])
model.fit(train_dataset, epochs=5, validation_data=val_dataset)

# Save the trained model weights
model.save_weights('gender_model_weights.h5')

# Load the trained model
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
model.load_weights('gender_model_weights.h5')

# Function to predict gender based on a name
def predict_gender(name):
    # Tokenize the input name
    encoding = tokenizer([name], truncation=True, padding=True)

    # Create TensorFlow dataset
    input_dataset = tf.data.Dataset.from_tensor_slices(dict(encoding)).batch(1)

    # Make predictions using the trained model
    predictions = model.predict(input_dataset)
    predicted_label = tf.argmax(predictions.logits, axis=1)[0].numpy()

    # Map the predicted label to gender
    gender = "male" if predicted_label == 0 else "female"

    return gender

# Get gender from user input
name = input("Enter a name: ")
predicted_gender = predict_gender(name)
print(f"The predicted gender for the name '{name}' is: {predicted_gender}")
