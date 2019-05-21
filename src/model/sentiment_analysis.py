
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
    sentiment_features = {}
    getSentimentScore(sentence, sentiment_features)
    return sentiment_features


def getSentimentScore(sentence, sentiment_features):
    tokens = nltk.word_tokenize(sentence)
    tokens = [(t.lower()) for t in tokens]
    try:
        text_blob = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
        sentiment_extraction = TextBlob(text_blob).sentiment
        sentiment_features['SentimentScore'] = sentiment_extraction.sentiment
        sentiment_features['SentimentSubjectivity'] = sentiment_extraction.subjectivity


    except:
        sentiment_features['SentimentScore'] = 0.0
        sentiment_features['SentimentSubjectivity'] = 0.0
