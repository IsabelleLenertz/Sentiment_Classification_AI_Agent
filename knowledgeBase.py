from pyknow import *

''' Global Variables used by the inference engine to score the two ML algorithms'''
''' The higher the score, the better the algorithm. Scoring depends on the user's preferences'''
scoreAlgo1 = 0
scoreAlgo2 = 0

class MLAlgo(Fact):
    """Info about the ML algorithms."""    
    pass

class userChoice(Fact):
    """Info about the user's choice"""

class ScoreAlgorithm(KnowledgeEngine):
    @Rule(Fact(accuracyScore = 10))
    def perfectAccuracy (self):
        print("Perfect accuracy!")
        
    @Rule(Fact(executionTimeScore = 10))
    def perfectExeTime(self):
        print("That training is hell of fast!")
    
    @Rule(Fact(executionTimeScore = 10) and Fact(accuracyScore = 10))
    def perfectAlgo(self):
        print("Perfect accuracy and great training time, nothing can eat that algorithm")


    