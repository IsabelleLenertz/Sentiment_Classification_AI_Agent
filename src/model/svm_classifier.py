#
# author : Jisha Pillai (jisha.pillai@sjsu.edu)
#
import csv
import nltk
import math
import time
import numpy as np
import pandas as pd
import model.sentiment_analysis
from sklearn import svm
from sklearn.utils import shuffle
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix



def main():
    results = model()
    print(results)

def model():
    start = time.time()
    features = []
    with open("../../training.csv", 'r') as file:
        lines = csv.reader(file, delimiter = ',')
        for line in lines:
            class_label, sentence = line
            features.append((sentiment_analysis.feature_extraction(sentence), class_label))

    featuresets=np.array(features)
    targets=(featuresets[0::,1])

    vec = DictVectorizer()
    featurevec = vec.fit_transform(featuresets[0::,0])

    #Shuffling the data
    order=shuffle(range(len(featuresets)))
    targets=targets[order]
    featurevec=featurevec[order,0::]

    #Train and Test data split
    size = int(len(featuresets) * .3)

    X_train = featurevec[size:,0::]
    y_train = targets[size:]
    X_test = featurevec[:size,0::]
    y_test = targets[:size]

    # Create a linear SVM classifier
    clf = svm.SVC(C=1, gamma='auto', class_weight=None, coef0=0.0, kernel='linear')

    # Train the classifier using the training data
    clf.fit(X_train, y_train)

    # Make predictions on the test data
    clf_predictions = clf.predict(X_test)

    # Calculate Accuracy
    accuracy = clf.score(X_test, y_test) * 100

    print("Accuracy of the model: ", "{0:.2f}".format(accuracy))

    cm = confusion_matrix(y_test, clf_predictions)

    # Calculate Sensitivity
    sensitivity = float(cm[0,0])/float(cm[0,0]+cm[0,1])
    print('Sensitivity : ', sensitivity )

    # Calculate Specificity
    specificity = float(cm[1,1]/float(cm[1,0]+cm[1,1]))
    print('Specificity : ', specificity)

    end = time.time()

    execution_time = float(end-start)
    print('Execution time in seconds', execution_time)

    return accuracy, sensitivity, specificity, execution_time





if __name__ == "__main__":
    main()
