# import re
# from nltk.corpus import stopwords
# import nltk
# nltk.download('stopwords')

# stop_words = set(stopwords.words('english'))

# def preprocess(text):
#     text = text.lower()
#     text = re.sub(r'[^\w\s]', '', text)
#     words = text.split()
#     words = [word for word in words if word not in stop_words]
#     return words

import re
import nltk
from nltk.corpus import stopwords

# Download only if not already present
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return words