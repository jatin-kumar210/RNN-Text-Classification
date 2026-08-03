# 🧠 RNN Text Classification

A Deep Learning-based **Text Classification** web application built using **TensorFlow, Keras, and Streamlit**. The application preprocesses user input, converts text into sequences using a trained tokenizer, and predicts sentiment using a Recurrent Neural Network (RNN).

## 🌐 Live Demo

**Live App:** https://rnn-text-classification.onrender.com

## 📖 Project Overview

This project demonstrates the implementation of a Recurrent Neural Network (RNN) for text sentiment classification. Users can enter text into a Streamlit interface, and the trained model predicts whether the sentiment is **Positive** or **Negative**.

## ✨ Features

- Deep Learning-based sentiment classification
- Interactive Streamlit web application
- Real-time predictions
- Text preprocessing and tokenization
- TensorFlow/Keras model
- Deployed on Render

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- Pickle
- Render

## 📂 Project Structure

```text
RNN-Text-Classification/
│── app.py
│── model.keras
│── tokenizer.pkl
│── requirements.txt
│── .python-version
│── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/jatin-kumar210/RNN-Text-Classification.git
```

Move into the project directory:

```bash
cd RNN-Text-Classification
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🎯 How to Use

1. Launch the application.
2. Enter a sentence in the text box.
3. Click **Predict**.
4. View the predicted sentiment.

## 📊 Model Information

- **Model:** Recurrent Neural Network (RNN)
- **Framework:** TensorFlow/Keras
- **Input Processing:** Tokenization & Sequence Padding
- **Output:** Sentiment Classification (Positive/Negative)

## 🔮 Future Improvements

- Improve model accuracy with larger datasets
- Add confidence scores
- Support multi-class sentiment analysis
- Add attention mechanism or LSTM/GRU models
- Docker deployment

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, improve the project, and submit a pull request.

## 👨‍💻 Author

**Jatin Kumar**

- GitHub: https://github.com/jatin-kumar210
- LinkedIn: *(Add your LinkedIn profile)*

---

⭐ **If you found this project useful, consider giving it a star!**
