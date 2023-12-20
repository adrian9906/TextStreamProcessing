

import time
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from db.Find import findDoc
from Processing.Pre_processing.pre_process import WordTokenizer
from Clasification.NaiveBayes import PredictNaiveBayes, trainingNaiveBayes
from Clustering.K_means import clusterinK_means
from Clasification.LogisticRegression import PredictLR, trainingLR


if __name__=="__main__":
    
    start = time.time()
    
    data = []
    
    label = []
    
    a = findDoc("ClasificationDataset",'CNN_News_Articles')
    
    for i in a:
        if 'Article text' in i:
            data.append(i['Article text'])
            label.append(i['Category'])
    
    data_train, data_test, label_train, label_test = train_test_split(data, label, test_size=0.2, random_state=42)

    
    # naiveBayesPipeline = trainingNaiveBayes(data_train,label_train)
    
    # naiveBayes = PredictNaiveBayes(naiveBayesPipeline,data_test)
    
    dataList=[]
    
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
    
    # clusters = len(set(label))

    # k_means = clusterinK_means(data,clusters)
    
    # for labels,cluster in k_means.items():
    #     print(f"Label {label}")
    
    modelLR = trainingLR(data_train, label_train)
    
    dataLR = PredictLR(modelLR, data_test)
    
    for i in range(0,len(data_test)):
        dicData={"text":data_test[i],
               "Predicction":dataLR[i]}
        dataList.append(dicData)
        
        
    df = pd.DataFrame(dataList)
    
    accuracy = accuracy_score(dataLR, label_test)
    
    print(df)
    
    print(f"The accuracy of the model is: {round((accuracy*100),ndigits=2)} %")