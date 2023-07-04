import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
# to run that code you need to get that model (gender_model_weights.h5). it's size is about 420Mb
# i cannot upload to github bcz of its size now you can download it from following link
# https://drive.google.com/file/d/1W0qq_wzSO30qMj2Re1gTtB5PdlEWXZTG/view?usp=sharing
# or may be you can train your own model to predict gender i have given you dataset of names about 96k 
# file name is (names_to_train.csv) and to train model i used Bert classifier There are many methods but Bert is more efficient.
# its code is also given in file (code_to_train_model.py)
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
model.load_weights('gender_model_weights.h5')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
def predict_gender(name):
    encoding = tokenizer([name], truncation=True, padding=True)
    input_dataset = tf.data.Dataset.from_tensor_slices(dict(encoding)).batch(1)
    predictions = model.predict(input_dataset)
    predicted_label = tf.argmax(predictions.logits, axis=1)[0].numpy()
    gender = "male" if predicted_label == 0 else "female"
    return gender