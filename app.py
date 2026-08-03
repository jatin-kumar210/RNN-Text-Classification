import streamlit as st
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -------------------------
# Load model and tokenizer
# -------------------------
model = tf.keras.models.load_model("model.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Same maxlen used during training
maxlen = 7

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(
    page_title="RNN Sentiment Classifier",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 RNN Sentiment Analysis")
st.write("Enter a sentence and predict whether it is **Positive** or **Negative**.")

text = st.text_area("Enter your text")

if st.button("Predict"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        seq = tokenizer.texts_to_sequences([text])
        pad = pad_sequences(seq, maxlen=maxlen, padding="post")

        prediction = model.predict(pad, verbose=0)[0][0]

        st.subheader("Prediction")

        if prediction >= 0.5:
            st.success(f"😊 Positive ({prediction:.2%})")
        else:
            st.error(f"😞 Negative ({1-prediction:.2%})")

        st.progress(float(prediction))