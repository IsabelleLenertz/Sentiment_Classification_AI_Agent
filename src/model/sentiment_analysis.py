#
# author : Jisha Pillai (jisha.pillai@sjsu.edu)
#
import nltk
import string
import numpy as np
import pandas as pd
from textblob import TextBlob
import csv, collections, os
nltk.download('punkt')
  


def feature_extraction(sentence):
    features = {}
    getSentimentScore(sentence, features)
    return features


def getSentimentScore(sentence, features):
    tokens = nltk.word_tokenize(sentence)
    tokens = [(t.lower()) for t in tokens]
    try:
        blob = TextBlob("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip())
        features['Blob sentiment'] = blob.sentiment.polarity
        features['Blob subjectivity'] = blob.sentiment.subjectivity
    except:
        features['Blob sentiment'] = 0.0
        features['Blob subjectivity'] = 0.0
