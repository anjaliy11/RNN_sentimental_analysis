# Step 1: Import Libraries and Load the Model
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load the pre-trained model with ReLU activation
model = load_model('simple_rnn_imdb.keras')

# Step 2: Helper Functions
# Function to decode reviews
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# ---------------------- STREAMLIT APP ----------------------

# Add background image and custom CSS
st.markdown(
    """
    <style>
    body {
        background-image: url("https://www.google.com/imgres?q=cinema%20hall%20popcorn&imgurl=https%3A%2F%2Fimg.freepik.com%2Fpremium-photo%2F3d-render-popcorn-with-cinema-time_252008-407.jpg&imgrefurl=https%3A%2F%2Fwww.freepik.com%2Fpremium-photo%2F3d-render-popcorn-with-cinema-time_13582066.htm&docid=436yS-8CwNJ_5M&tbnid=RJDSke6zXTwkjM&vet=12ahUKEwi68eax1dWPAxWKUWwGHbkcG1UQM3oECHIQAA..i&w=626&h=352&hcb=2&ved=2ahUKEwi68eax1dWPAxWKUWwGHbkcG1UQM3oECHIQAA");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .main-title {
        font-size: 40px;
        text-align: center;
        font-weight: bold;
        color: #FFD700;
    }
    .result-box {
        padding: 20px;
        margin-top: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }
    .positive {
        background-color: rgba(0, 128, 0, 0.6);
    }
    .negative {
        background-color: rgba(220, 20, 60, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="main-title">🎬 IMDB Movie Review Sentiment Analysis 🎭</div>', unsafe_allow_html=True)
st.write("Enter a movie review below to classify it as **Positive** or **Negative**.")

# User input
user_input = st.text_area('✍️ Write your movie review here:')

# Button
if st.button('🔍 Classify'):
    if user_input.strip() != "":
        preprocessed_input = preprocess_text(user_input)

        # Make prediction
        prediction = model.predict(preprocessed_input)
        sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

        # Display the result with styled box
        css_class = "positive" if sentiment == "Positive" else "negative"
        st.markdown(
            f'<div class="result-box {css_class}">Sentiment: {sentiment}<br>Prediction Score: {prediction[0][0]:.4f}</div>',
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please enter a review before classifying.")
else:
    st.info("👉 Type a review and click **Classify** to see the sentiment.")
