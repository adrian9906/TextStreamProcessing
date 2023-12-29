import string
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


nltk.download('stopwords')
def WordTokenizer(text):
    stopWords = set(stopwords.words('english')) 
    
    stopWords =stopWords.union(set(string.punctuation))
    word_tokenizer = TweetTokenizer()
    
    tokens = word_tokenizer.tokenize(text)
    
    tokens = [token for token in tokens if token not in stopWords]
    
    return tokens
