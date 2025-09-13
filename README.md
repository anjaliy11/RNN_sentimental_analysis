# 🎭 RNN Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Keras](https://img.shields.io/badge/Keras-Deep--Learning-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview
This project implements a **Simple Recurrent Neural Network (RNN)** model for **sentiment analysis** on the IMDB movie review dataset.  
The model classifies reviews as **positive** or **negative** based on textual input.

It also includes a **Streamlit web app** that allows users to input custom reviews and receive predictions in real time.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Quickstart](#-quickstart)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Contribution](#-contribution)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## ⚡ Quickstart

### 🔹 Clone Repository
```bash
git clone https://github.com/anjaliy11/RNN_sentimental_analysis.git
cd RNN_sentimental_analysis
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Train the Model
```bash
jupyter notebook
simple_rnn.ipynb
prediction.ipynb
```

### 🔹 Run the Streamlit App
```bash
streamlit run main.py
```

---

## ✨ Features
✅ Train an **RNN** on the IMDB dataset  
✅ Sentiment classification (**Positive / Negative**)  
✅ Interactive **Streamlit app** for real-time predictions  
✅ Preprocessing of text using **word embeddings and padding**  
✅ High accuracy model with user-friendly interface  

---

## 📂 Project Structure
```
RNN_sentimental_analysis/
│── main.py                 # Streamlit app for predictions
│── simple_rnn.ipynb                # Training script for RNN model
│── simple_rnn_imdb.keras   # Saved model file
│── requirements.txt        # Required dependencies
│── README.md               # Project documentation
```

---

## 🗺 Roadmap
- [ ] Improve model generalization with LSTM/GRU  
- [ ] Add more datasets for robust sentiment classification  
- [ ] Enhance UI with advanced visualization  
- [ ] Deploy app on cloud (Heroku/Streamlit Cloud)  

---

## 🤝 Contribution
Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Open a Pull Request  

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements
- [TensorFlow](https://www.tensorflow.org/)  
- [Keras](https://keras.io/)  
- [IMDB Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)  
- [Streamlit](https://streamlit.io/)  

---
