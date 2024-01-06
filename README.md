# TextStreamProcessing
The TextStreamProcessing project is a comprehensive solution for processing text streams. This application implements a variety of natural language processing tasks, including text classification, clustering and zero-shot text classification.

***

# Dataset
The project uses the "cnn-articles" dataset available on [Kaggle](https://www.kaggle.com/datasets/hadasu92/cnn-articles-after-basic-cleaning). This dataset contains CNN articles after basic cleaning. For efficient storage and retrieval, MongoDB was used to store the training dataset.

***
# Features
1. Text classification using the Naive Bayes and Logistic Regression classifiers.
2. Text clustering using the K-Means algorithm.
3. Use of Word2Vec for classification with Logistic Regression.
4. Use of TF-IDF for Naive Bayes and Logistic Regression.
5. Text clasificaction using Bert Transformer model.

***

# Dependencies
This project requires the following Python libraries:
1. NumPy
2. Scikit-learn
3. NLTK
4. Gensim
5. pymongo
6. Trasformers

***

# Usage
The project can be used to classify and cluster texts. The specific details of how to do this will depend on your specific needs.

***
# Getting Started
To start using this project, follow these steps:

1. Clone the repository into your local machine.
2. Install the necessary dependencies.
3. Run the __init__ script.

***

# Accuracy
The accuracy results of the classifiers are as follows:

1. Naive Bayes: 85%
2. Logistic Regression: 92%
3. Logistic Regression with Word2Vect: 60%
4. Bert Clasification: 84%

# Contributing
Contributions are welcome. Please open a pull request if you wish to contribute to the project.

***
# License
This project is licensed under the MIT License. See the LICENSE file for more details.
