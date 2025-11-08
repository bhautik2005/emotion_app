# emotion_app

# Text Emotion Detection App 🎭

A Flask-based web application that detects emotions from text using machine learning.

## 🌟 Features

- Real-time emotion classification
- Text preprocessing for better accuracy
- Simple and intuitive web interface
- Built with Flask and Scikit-learn

## 🧠 Demo_1
![Emotion Detection Output](https://github.com/bhautik2005/emotion_app/blob/0f1cca29cb8c50884ccd100c05935371dbe113d0/Screenshot%202025-11-08%20183456.png)
## 🧠 Demo_2
![Emotion Detection Output](https://github.com/bhautik2005/emotion_app/blob/4c3a715812d6192bc709946de3ac1305efd6df4b/image.jpg)
## 🛠️ Tech Stack

- Python 3.8+
- Flask
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/bhautik2005/emotion_app.git
cd emotion_app
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Flask server:
```bash
python app/main.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

3. Enter your text and click "Predict" to see the emotion!

## 📁 Project Structure

```
├── model/
│   ├── lr.pkl              # Trained model
│   ├── tfidf_vectorizer.pkl
│   └── emotion_labels.pkl
├── app/
│   ├── preprocess.py       # Text preprocessing
│   └── main.py            # Flask application
├── templates/
│   └── index.html         # Web interface
└── static/
    └── style.css         # Styling
```

## 🤝 Contributing

Feel free to open issues and pull requests!

## 📝 License

This project is licensed under the MIT License.
Copyright (c) 2025 Bhautik Gondaliya
