import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

text = "Tokenization is important for NLP."
doc = nlp(text)

# Word Tokens
word_tokens = [token.text for token in doc]
print(word_tokens)  # Output: ['Tokenization', 'is', 'important', 'for', 'NLP', '.']

# Sentence Tokens
sent_tokens = list(doc.sents)
print([sent.text for sent in sent_tokens])  # Output: ['Tokenization is important for NLP.']
