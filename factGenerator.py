from knowledgeBase import *
from pyknow import *

def ETS(executionTime):
    if executionTime < 500:
        return 10
    else:
        return 0

def TTS(trainingTime):
    if trainingTime < 1000:
        return 10
    else:
        return 0
    return None
   
def AccuracyScoring(accuracy):
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
    engine.declare(Fact(accuracyScore = AccuracyScoring(algorithm.accuracy)))
    engine.declare(Fact(traingTimeScore = TTS(algorithm.trainingTime)))
    engine.declare(Fact(executionTimeScore = ETS(algorithm.executionTime)))
    