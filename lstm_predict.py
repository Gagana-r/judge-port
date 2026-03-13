import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

MAXLEN = 100

# Load model and tokenizer
model = tf.keras.models.load_model("lstm_model.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

def predict_lstm(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAXLEN)
    pred = model.predict(padded)[0]
    return ["Negative", "Neutral", "Positive"][np.argmax(pred)]
