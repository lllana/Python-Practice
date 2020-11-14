import nltk
from nltk.stem import WordNetLemmatizer
import pandas as pd
from collections import Counter

feedback=pd.read_csv('/datasets/feedback_eng.csv')
wordnet_lemma = WordNetLemmatizer()

words = nltk.word_tokenize(feedback['text'][1])

lemmas = [wordnet_lemma.lemmatize(w, pos = 'n') for w in words]

print(lemmas)
print(Counter(lemmas))