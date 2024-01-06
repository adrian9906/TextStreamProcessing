

import time
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from db.Find import findDoc
from Processing.Pre_processing.pre_process import WordTokenizer
from Clasification.NaiveBayes import PredictNaiveBayes, trainingNaiveBayes
from Clustering.K_means import clusterinK_means
from Clasification.LogisticRegression import PredictLR, trainWordEmeddings, trainingLR
from Processing.Feature_Selection.WordEmbeddings.word2Vec_Model import trainWord2Vec
from Clasification.BertClasification import Ber_Clasification_Train, PredictBertClasification
from Processing.Feature_Selection.WordEmbeddings.BertModel import loadBertModel


if __name__=="__main__":
    
    start = time.time()
    
    data = []
    
    label = []
    
    a = findDoc("ClasificationDataset","CNN_News_Articles")
    
    for i in a:
        if 'Article text' in i:
            data.append(i['Article text'])
            label.append(i['Category'])
    
    data_train, data_test, label_train, label_test = train_test_split(data, label, test_size=0.2, random_state=42)
    dataList=[]
    
    ############### Naive Bayes ###################
    
    # naiveBayesPipeline = trainingNaiveBayes(data_train,label_train)
    
    # naiveBayes = PredictNaiveBayes(naiveBayesPipeline,data_test)
    
    
    
    # for i in range(0,len(data_test)):
    #     dicData={"text":data_test[i],
    #              "Predicction":naiveBayes[i]}
    #     dataList.append(dicData)
    
    # df = pd.DataFrame(dataList)
    
    # end = time.time()
    
    # accuracy = accuracy_score(naiveBayes, label_test)
    
    # print(df)
    
    # print(f"Took: {end-start} to Naive Bayes predict {len(data_test)}")
    
    # print(f"The accuracy of the model is: {round((accuracy*100),ndigits=2)} %")
    
    ############### K-means ###################
    
    # clusters = len(set(label))

    # k_means = clusterinK_means(data,clusters)
    
    # for labels,cluster in k_means.items():
    #     print(f"Label {label}")
    
    ############### Logistic Regression ###################
    
    # modelLR = trainingLR(data_train, label_train)
    
    # dataLR = PredictLR(modelLR, data_test)
    
    # for i in range(0,len(data_test)):
    #     dicData={"text":data_test[i],
    #            "Predicction":dataLR[i]}
    #     dataList.append(dicData)
        
        
    # df = pd.DataFrame(dataList)
    
    # accuracy = accuracy_score(dataLR, label_test)
    
    # print(df)
    
    # print(f"The accuracy of the model is: {round((accuracy*100),ndigits=2)} %")
    
    ############### Logistic Regression word2vec ###################
    
    # arrayWord2vec = trainWord2Vec(data_train)
    
    # arrayWord2vecTest = trainWord2Vec(data_test)
    
    # modelLRW2V = trainWordEmeddings(arrayWord2vec, label_train)
    
    # pred = modelLRW2V.predict(arrayWord2vecTest)
    
    # accuracy = accuracy_score(pred, label_test)
    
    # print(f"The accuracy of the model is: {round((accuracy*100),ndigits=2)} %")
    
tokenizer, model = loadBertModel(label)
modelo, labelCoder = Ber_Clasification_Train(data_train,label_train,model, tokenizer)

df2, lab2 = PredictBertClasification(data_test, modelo, labelCoder, tokenizer)

print(df2)

accuracy = accuracy_score(df2['label'], label_test)

print(accuracy)
    
    