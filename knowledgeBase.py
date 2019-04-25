from pyknow import *

algo1Score = 0
algo2Score = 0

class MLAlgo(Fact):
    """Info about the ML algorithms."""    
    pass

class userChoice(Fact):
    """Info about the user's choice"""

class GetBestAlgo(KnowledgeEngine):
    @Rule(Fact(accuracyScore = 10))
    def perfectAccuracy (self):
        print("Perfect accuracy!")
        
    @Rule(Fact(executionTimeScore = 10))
    def perfectExeTime(self):
        print("That training is hell of fast!")
    
    @Rule(AND(Fact(executionTimeScore = 10), Fact(accuracyScore = 0)))
    def perfectAlgo(self):
        print("Perfect accuracy and great training time, nothing can eat that algorithm")


    