import knowledgeBase
import factGenerator
import model.svm_classifier as svm_classifier
import bagOfWordsModel.train as bagOfWord
from pyknow import *

""" Makes sure changes in imported files are carried out"""
import importlib
importlib.reload(knowledgeBase)
importlib.reload(factGenerator)
importlib.reload(svm_classifier)
importlib.reload(bagOfWord)



class Algorithm():
    def __init__(self, classifier, accuracy, executionTime, sensitivity, specificity):
        self.classifier = classifier
        self.accuracy = accuracy
        self.executionTime = executionTime
        self.sensitivity = sensitivity
        self.specificity = specificity

""" Introduction to the AI agent """
print("Welcome to our smart classifier")
print("The AI agent classifies messages as positive and negative using sentiment analysis")
print("Would you prefer the algorithm to be as precise as possible or as fast as possible?")

 # run algo 1, return classifier and performance info

 # run algo 2, return classifier and performance info

 # Get user's choice of most important feature
userChoice = "";
while(userChoice != "p" and userChoice != "s"):
    userChoice = input("[p]recision, [s]peed: ")

#Creating models
print("Creating new models...");
print("... please wait...");
print("");
print("Training SVM Model...");
#create svm model
classifier, accuracy, sensitivity, specificity, execution_time = svm_classifier.model();
algo1 = Algorithm('SVM classifier', accuracy, execution_time,sensitivity, specificity) #for testing purposes

print("")
print("Training Random Forest Model...")
#create bag of world model
accuracy, sensitivity, specificity, execution_time = bagOfWord.model();
algo2 = Algorithm('Random Forest classifier', accuracy, execution_time,sensitivity, specificity) #for testing purposes
scores = {};
print("");
print("Done training the models");

""" Run and score the first algorithm"""
engine = factGenerator.ScoreAlgorithm();
engine.reset();
engine.declare(Fact(userChoice));
factGenerator.GenerateFacts(engine, algo1)
engine.run();
scores[algo1] = knowledgeBase.score
knowledgeBase.score = 0

""" Run and score the second algorithm"""
engine2 = factGenerator.ScoreAlgorithm();
engine2.reset();
engine.declare(Fact(userChoice));
factGenerator.GenerateFacts(engine2, algo2)
engine2.run();
scores[algo2] = knowledgeBase.score
knowledgeBase.score = 0

""" Get the algorithm with the highest score """
chosenAlgo = max(scores, key = lambda k: scores[k])
print("Recommending: " + chosenAlgo.classifier)

""" Asking for text to  classify and classify it """
#text = input("enter the text you want to classify: ")
#print(classifier1.predict(text));
#TODO classify
