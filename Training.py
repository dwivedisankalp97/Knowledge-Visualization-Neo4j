import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn import tree
from sklearn.metrics import accuracy_score

np.random.seed(500)
Corpus = pd.read_csv(r"D:\Capstone\trainingdata.csv",encoding='latin-1')
print("Shape:", Corpus.shape)
print("\nFeatures", Corpus.columns)
X = Corpus[Corpus.columns[:-1]] 
y = Corpus[Corpus.columns[-1]] 
# printing first 5 rows of feature matrix 
print("\nFeature matrix:\n", X.head()) 
  
# printing first 5 values of response vector 
print("\nResponse vector:\n", y.head())

#Remove blank rows if any.
Corpus['text'].dropna(inplace=True)
#Change all the text to lower case.
Corpus['text'] = [entry.lower() for entry in Corpus['text']]
#Tokenization
Corpus['text']= [word_tokenize(entry) for entry in Corpus['text']]
#Remove Non-Numeric entries and perfom Word Lemmatization. WordNetLemmatizer requires Pos tags to understand if the word is noun or verb or adjective etc. By default it is set to Noun
tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV
for index,entry in enumerate(Corpus['text']):
    # Declaring Empty List to store the words that follow the rules for this step
    Final_words = []
    # Initializing WordNetLemmatizer()
    word_Lemmatized = WordNetLemmatizer()
    # pos_tag function below will provide the 'tag' i.e if the word is Noun(N) or Verb(V) or something else.
    for word, tag in pos_tag(entry):
        # Below condition is to check for alphabets
        if word not in stopwords.words('english') and word.isalpha():
            word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
            Final_words.append(word_Final)
    # The final processed set of words for each iteration will be stored in 'ftext'
    Corpus.loc[index,'ftext'] = str(Final_words)
#print("here",Corpus['ftext'])

Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus['ftext'],Corpus['label'],test_size=0.1)

Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(Train_Y)
Test_Y = Encoder.fit_transform(Test_Y)
print(Test_X)
Tfidfv = TfidfVectorizer(ngram_range=(1,4))
Tfidffit = Tfidfv.fit(Corpus['ftext'])
Train_X_Tfidf = Tfidfv.transform(Train_X)
print(Train_X_Tfidf)
Test_X_Tfidf = Tfidfv.transform(Test_X)
#print(Tfidfv.vocabulary_)
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_NB = Naive.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, Test_Y)*100)
# Classifier - Algorithm - SVM
# fit the training dataset on the classifier
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_SVM = SVM.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(Train_X_Tfidf,Train_Y)
predictions_clf = clf.predict(Test_X_Tfidf)
print("Tree Accuracy Score -> ",accuracy_score(predictions_clf, Test_Y)*100)

import pickle
savefile = "trainedmodel.sav"
tfidfsav = "tfidffit.pickle"
pickle.dump(SVM,open(savefile,"wb"))
pickle.dump(Tfidffit,open(tfidfsav,"wb"))

# fit the training dataset on the NB classifier
'''
count_vect = CountVectorizer(stop_words="english", analyzer='word', 
                            ngram_range=(1, 4))
count_vect.fit(Corpus['ftext'])
Train_X_Count = count_vect.transform(Train_X)
Test_X_Count = count_vect.transform(Test_X)
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Count,Train_Y)
# predict the labels on validation dataset
predictions_NB = Naive.predict(Test_X_Count)
# Use accuracy_score function to get the accuracy
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, Test_Y)*100)
# Classifier - Algorithm - SVM
# fit the training dataset on the classifier
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Count,Train_Y)
# predict the labels on validation dataset
predictions_SVM = SVM.predict(Test_X_Count)
# Use accuracy_score function to get the accuracy
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(Train_X_Count,Train_Y)
predictions_clf = clf.predict(Test_X_Count)
print("Tree Accuracy Score -> ",accuracy_score(predictions_clf, Test_Y)*100)
'''
