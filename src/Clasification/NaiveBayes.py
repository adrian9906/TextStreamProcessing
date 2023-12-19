from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from db.Find import findDoc

def trainingNaiveBayes(corpus,labels):
    
    pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer(smooth_idf=True, use_idf=True)),
    ('clf', MultinomialNB()),
    ])
    
    finalPipeline = pipeline.fit(corpus,labels)
    
    return finalPipeline

def PredictNaiveBayes(pipeline, text):
    
    dfPredict = pipeline.predict(text)
   
    return dfPredict


