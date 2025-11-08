import joblib
from app.preprocess import preprocess_text

# Load models
lr = joblib.load('model/lr.pkl')
tfidf = joblib.load('model/tfidf_vectorizer.pkl')
emotion_labels = joblib.load('model/emotion_labels.pkl')

# If keys are reversed (like 'sadness':0,...)
if list(emotion_labels.keys())[0] == 'sadness':
    emotion_labels = {v: k for k, v in emotion_labels.items()}

# Test sentences
test_texts = [
    "I am very happy today!",
    "I feel sad and lonely.",
    "I love spending time with my family.",
    "I am so scared of the dark.",
    "I can’t believe I won the prize!",
    "I hate when people lie to me."
]

print("🔍 Emotion Detection Test\n")
for text in test_texts:
    processed = preprocess_text(text)
    vectorized = tfidf.transform([processed])
    prediction = lr.predict(vectorized)[0]
    label = emotion_labels[prediction]
    print(f"Input: {text}\nProcessed: {processed}\nPredicted Emotion: {label}\n")
