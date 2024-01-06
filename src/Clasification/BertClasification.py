from cv2 import _InputArray_STD_BOOL_VECTOR
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import DataLoader
from transformers import AdamW
#from Processing.Feature_Selection.WordEmbeddings.BertModel import loadBertModel

def Ber_Clasification_Train(dataSet,labels,model , tokenizer):
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    inputs = tokenizer(dataSet, padding=True, truncation=True, return_tensors="pt",)
    
    dataset = list(zip(inputs["input_ids"], inputs["attention_mask"], labels))
    loader = DataLoader(dataset, batch_size=2, shuffle=True)
    
    optimizer = AdamW(model.parameters(), lr=1e-5)
    
    model.train()
    for epoch in range(3):  # Choose appropriate number of epochs
        for batch in loader:
            input_ids, attention_mask, labels = batch
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
    
    return model, le

def PredictBertClasification(texts, model,labelEncoder, tokenizer):
    listData = []
    inputs2 = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    logits = model(**inputs2).logits
    predictions = logits.argmax(dim=1)
    predictionsLabels = labelEncoder.inverse_transform(predictions)
    
    for i in range(len(texts)):
        data = {
            'text': texts[i],
            'label': predictionsLabels[i] 
        }
        listData.append(data)
        
    df = pd.DataFrame(listData)
    
    return df, predictionsLabels


