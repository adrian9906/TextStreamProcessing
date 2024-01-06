from transformers import BertTokenizer, BertForSequenceClassification

def loadBertModel(labels):
    label = len(set(labels))
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased',num_labels = label )
    return tokenizer, model