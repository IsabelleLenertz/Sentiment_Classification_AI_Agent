from knowledgeBase import *
from pyknow import *
from factGenerator import *

class Algorithm():
    def __init__(self, classifier, accuracy, trainingTime, executionTime, sensitivity, specificity):
        self.classifier = classifier
        self.accuracy = accuracy
        self.trainingTime = trainingTime
        self.executionTime = executionTime
        self.sensisitivity = sensitivity
        self.specificity = specificity


 # run algo 1, return classifier and performance info
 
 # run algo 2, return classifier and performance info
algo = Algorithm('classifier', 1, 1, 0.3, 0.9, 0.9)
engine = GetBestAlgo();
engine.reset();
GenerateFacts(engine, algo)
engine.run();