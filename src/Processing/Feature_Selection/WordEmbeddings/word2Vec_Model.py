from gensim.models import Word2Vec
import numpy as np

from Processing.Pre_processing.pre_process import WordTokenizer

def trainWord2Vec(document):
    sentences = []
    for docu in document:
        sentences.append(WordTokenizer(docu))  
    
    w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=3, workers=4)  
    sentence_vectors = []
    for sentence in sentences:
        vector = [w2v_model.wv[word] for word in sentence if word in w2v_model.wv]
        if len(vector) == 0:
            print(sentence)
            sentence_vectors.append(np.zeros(100))
            continue
        words_vecs = np.array(vector)
        words_vecs = words_vecs.mean(axis=0)
        sentence_vectors.append(words_vecs)
    
    return sentence_vectors