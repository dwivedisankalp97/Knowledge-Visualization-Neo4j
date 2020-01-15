import pickle
import os
import sys
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize,sent_tokenize
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

fileDir = os.path.dirname(os.path.realpath('__file__'))
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

SVM = pickle.load(open("trainedmodel.sav","rb"))
filename = os.path.join(fileDir, 'Prediction Dataset/predictionresult.txt')
f = open(filename,"w")
predictfile = open("articles1.txt","r",encoding ="utf8")
word_Lemmatized = WordNetLemmatizer()
for line in predictfile:
    #print(line)
    if(len(line)<=5):
        continue
    temp = line
    line = sent_tokenize(line)
    #print("here",line)
    Final_words = []
    Final_lines = []
    line = [entry.lower() for entry in line]
    line = [word_tokenize(entry) for entry in line]
    #print(line)
    #Remove Non-Numeric entries and perfom Word Lemmatization. WordNetLemmatizer requires Pos tags to understand if the word is noun or verb or adjective etc. By default it is set to Noun
    tag_map = defaultdict(lambda : wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    for entry in line:
        #print("entry in line +=",entry)
        tempp = " "
        tempp = tempp.join(entry)
        Final_words = []
        for word,tag in pos_tag(entry):
            if word.isalpha():
                word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
                Final_words.append(word_Final)
                #print(Final_words)
        finalline = str(Final_words)
        Final = [finalline]
        #print("final line = ", Final)
        #print("here")
        Tfidfv = pickle.load(open("tfidffit.pickle","rb"))
        Test = Tfidfv.transform(Final)
        prediction = SVM.predict(Test)
        print(prediction[0])
        if prediction[0] == 1:
            #print("helkrjlsakdjf")
            #print(temp)
            f = open(filename,"a",encoding='utf8')
            ##print(tempp)
            tempp = tempp.translate(non_bmp_map)
            f.write(tempp)
        #print("Here")
    f.close()
        
    
