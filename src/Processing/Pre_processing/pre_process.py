import string
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


nltk.download('stopwords')
def WordTokenizer(text):
    
    word_tokenizer = TweetTokenizer()
    
    tokens = word_tokenizer.tokenize(text)
    
    return tokens

def RemoveStopWords(text):
    
    stopWords = set(stopwords.words('english')) 
    
    stopWords =stopWords.union(set(string.punctuation))
    
    return ''.join([token for token in text if token.lower() not in stopWords])

