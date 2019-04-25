from knowledgeBase import *
from pyknow import *
from factGenerator import *


class Algorithm():
    def __init__(self, classifier, accuracy, trainingTime, executionTime, sensitivity, specificity):
        self.classifier = classifier
        self.accuracy = accuracy
        self.trainingTime = trainingTime
        self.executionTime = executionTime
        self.sensitivity = sensitivity
        self.specificity = specificity


 # run algo 1, return classifier and performance info
 
 # run algo 2, return classifier and performance info
 
 #Get user's choice of most important feature
 
algo1 = Algorithm('classifier', 1, 1, 0.3, 0.9, 0.9) #for testing purposes
algo2 = Algorithm('classifier', 1, 1, 0.3, 0.9, 0.9) #for testing purposes

engine = ScoreAlgorithm();
engine.reset();
GenerateFacts(engine, algo1, 1)
engine.run();

engine2 = ScoreAlgorithm();
engine2.reset();
GenerateFacts(engine2, algo2, 2)
engine2.run();