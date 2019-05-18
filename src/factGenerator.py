from knowledgeBase import *
from pyknow import *

def specificityScoring(specificity):
    ''' Define some rules to score the specificity'''
    if specificity > 0.7:
        return "specific"
    if specificity > 0.5:
        return"barely specific"
    return "specificity worst than random"

def sensitivyScoring(sensistivity):
    ''' Define some rules to score the sensitivity'''
    if sensistivity > 0.7:
        return "sensitive"
    if sensistivity > 0.5:
        return"barely sensitive"
    return "sensitivy worst than random"

def ETS(executionTime):
    ''' Define some rules to score the execution time'''
    if executionTime < 1:
        return 10
    elif executionTime < 2:
        return 9
    elif executionTime < 3:
        return 8
    elif executionTime < 4:
        return 6
    elif executionTime < 5:
        return 5
    elif executionTime < 6:
        return 4
    elif executionTime < 7:
        return 0

def AccuracyScoring(accuracy):
    ''' Define some rules to score the accuracy'''
    if accuracy < 0.1:
        return 0
    elif accuracy < 0.2:
        return 1
    elif accuracy < 0.3:
        return 2
    elif accuracy < 0.4:
        return 3
    elif accuracy < 0.5:
        return 4
    elif accuracy < 0.6:
        return 5
    elif accuracy < 0.7:
        return 6
    elif accuracy < 0.8:
        return 7
    elif accuracy < 0.9:
        return 8
    elif accuracy < 1:
        return 9
    else:
        return 10
        
def GenerateFacts(engine, algorithm):
    ''' Generate the facts about one algorithm in the knowledge base'''
    engine.declare(Fact(accuracyScore = AccuracyScoring(algorithm.accuracy)))
    engine.declare(Fact(executionTimeScore = ETS(algorithm.executionTime)))
    engine.declare(Fact(specificity  = specificityScoring(algorithm.specificity)))
    engine.declare(Fact(sensitivity = sensitivyScoring(algorithm.sensitivity)))
    