import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

#tokenozation        ----> Breaking a text into smaller managable pieces
#word,sent_tokenize  ----> tokenize a text into words and sentence respectively
#Stemming            ----> Finding the base/root word (root word may not be actually used word)
#Lemmatization       ----> Finding the base/root word on dictionary-based approach
#PorterStemmer       ----> Stemming algorithm
#WordNetLemmatizer   ----> WordNet lexiacal DB to perform lemmatization

text = "Hello there! How are you doing today?"
print(word_tokenize(text))
print(sent_tokenize(text))

#Creates Instances(object) of the classes
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

word = "running"
print(stemmer.stem(word))  
print(lemmatizer.lemmatize("eating", pos='v')) #v  ----> Verb n ----> Noun a ----> Adjective r ---->Adverb

