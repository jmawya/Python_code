import nltk

nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

text = "I am learning Natural Language Processing by using Python."

tokens = word_tokenize(text)
print(tokens)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Natural Language Processing is very interesting and useful"

# Tokenize text
words = word_tokenize(text)

# Load English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_words = [word for word in words if word.lower() not in stop_words]

print(filtered_words)
