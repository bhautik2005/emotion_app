import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure resources
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_numbers(text):
    return re.sub(r'\d+', '', text)

def remove_stopwords(text):
    word_tokens = word_tokenize(text)
    return ' '.join([word for word in word_tokens if word.lower() not in stop_words])

def preprocess_text(text):
    text = text.lower()
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = remove_stopwords(text)
    return text
