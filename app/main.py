from flask import Flask, render_template, request
import joblib
from preprocess import preprocess_text

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer
lr_model = joblib.load('model/lr_model.pkl')
tfidf_vectorizer = joblib.load('model/tfidf_vectorizer.pkl')
emotion_labels = joblib.load('model/emotion_labels.pkl')  # {0:'sadness',1:'joy',...}
# Invert mapping: {0:'sadness', 1:'anger', ...}
emotion_labels = {v: k for k, v in emotion_labels.items()}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    processed_text = preprocess_text(text)
    tfidf_input = tfidf_vectorizer.transform([processed_text])
    prediction_numeric = lr_model.predict(tfidf_input)[0]
    prediction_label = emotion_labels[prediction_numeric]

    return render_template('index.html', 
                           original_text=text, 
                           processed_text=processed_text,
                           prediction=prediction_label)

if __name__ == '__main__':
    app.run(debug=True)
