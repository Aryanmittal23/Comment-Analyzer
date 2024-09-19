import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary resources
nltk.download('punkt')

text = "Hello world! I love NLP."

# Word Tokenization
word_tokens = word_tokenize(text)
print(word_tokens)  # Output: ['Hello', 'world', '!', 'I', 'love', 'NLP', '.']

# Sentence Tokenization
sent_tokens = sent_tokenize(text)
print(sent_tokens)  # Output: ['Hello world!', 'I love NLP.']
