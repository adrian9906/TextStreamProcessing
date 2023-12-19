import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def clusterinK_means(text, i):
    vectorizer = TfidfVectorizer()
    
    clusterData = vectorizer.fit_transform(text)
    
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(clusterData)
    
    labels = kmeans.labels_
    
    categories = {label: [] for label in set(labels)}
    
    for document, label in zip(text, labels):
        categories[label].append(document)
        
        
        
    return categories