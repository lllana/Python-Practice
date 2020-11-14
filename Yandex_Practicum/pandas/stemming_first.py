from nltk.stem import SnowballStemmer
english_stemmer = SnowballStemmer('english')

queries = ["apple iphone", 
           "buy apple iphone", 
           "best smartphones", 
           "baron phone", 
           "smartphone apple iphone", 
           "smartphones 2019", 
           "pineapple", 
           "background music", 
           "apple iphone x", 
           "apple iphone 64gb",
           "specialist in phonetics",
           "buy apple",
           "apple iphone buy",
           "snapple", 
           "smartphone buy where", 
           "dappled deer", 
           "smartphone huawei",
           "apple"]

for query in queries:
    for word in query.split(" "):
        stemmed_word = english_stemmer.stem(word)
        if stemmed_word == 'appl':
            print(query)