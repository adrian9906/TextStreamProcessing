from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def trainingLR(corpus,labels):
    
    pipeline = Pipeline([
   ('vectorizer', CountVectorizer()),
   ('tfidf', TfidfTransformer(smooth_idf=True, use_idf=True)),
   ('classifier', LogisticRegression(solver='lbfgs', max_iter=1000))
])
    
    finalPipeline = pipeline.fit(corpus,labels)
    
    return finalPipeline

def PredictLR(pipeline, text):
    
    dfPredict = pipeline.predict(text)
   
    return dfPredict
