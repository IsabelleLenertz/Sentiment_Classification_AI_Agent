from pyknow import *

''' Global Variables used by the inference engine to score the two ML algorithms'''
''' The higher the score, the better the algorithm. Scoring depends on the user's preferences'''
score = 0

class MLAlgo(Fact):
    """Info about the ML algorithms."""    
    pass

class userChoice(Fact):
    """Info about the user's choice"""

class ScoreAlgorithm(KnowledgeEngine):
    """ Scoring the accuracy for choice precision"""
    @Rule(Fact("p") and Fact(accuracyScore = 10))
    def perfectAccuracy (self):
        global score
        score = score*100;
    
    @Rule(Fact("p") and Fact(accuracyScore = 9))
    def perfectAccuracy (self):
        global score
        score = score*90;
        
    @Rule(Fact("p") and Fact(accuracyScore = 8))
    def perfectAccuracy (self):
        global score
        score = score*80;   
    @Rule(Fact("p") and Fact(accuracyScore = 7))
    def perfectAccuracy (self):
        global score
        score = score*70;
        
    @Rule(Fact("p") and Fact(accuracyScore = 6))
    def perfectAccuracy (self):
        global score
        score = score*60;
    @Rule(Fact("p") and Fact(accuracyScore = 5))
    def perfectAccuracy (self):
        global score
        score = score*50;
    #low accuracy set the score to 0 this is not tolerable
    @Rule(Fact("p") and (Fact(accuracyScore = 4) or Fact(accuracyScore = 3) or Fact(accuracyScore = 2) or Fact(accuracyScore = 1) or Fact(accuracyScore = 0)))
    def perfectAccuracy (self):
        global score
        score = score*0;  
    
    """ Scoring the Accuracy for choice speed"""
    @Rule(Fact("s") and Fact(accuracyScore = 10))
    def perfectAccuracy (self):
        global score
        score = score*10;
    
    @Rule(Fact("s") and Fact(accuracyScore = 9))
    def perfectAccuracy (self):
        global score
        score = score*9;
        
    @Rule(Fact("s") and Fact(accuracyScore = 8))
    def perfectAccuracy (self):
        global score
        score = score*8;   
    @Rule(Fact("s") and Fact(accuracyScore = 7))
    def perfectAccuracy (self):
        global score
        score = score*7;
        
    @Rule(Fact("s") and Fact(accuracyScore = 6))
    def perfectAccuracy (self):
        global score
        score = score*6;
    @Rule(Fact("s") and Fact(accuracyScore = 5))
    def perfectAccuracy (self):
        global score
        score = score*5;
    @Rule(Fact("s") and Fact(accuracyScore = 4))
    def perfectAccuracy (self):
        global score
        score = score*4;   
    @Rule(Fact("s") and Fact(accuracyScore = 3))
    def perfectAccuracy (self):
        global score
        score = score*3;
    @Rule(Fact("s") and Fact(accuracyScore = 2))
    def perfectAccuracy (self):
        global score
        score = score*2;
    @Rule(Fact("s") and Fact(accuracyScore = 1))
    def perfectAccuracy (self):
        global score
        score = score*1;
    @Rule(Fact("s") and Fact(accuracyScore = 0))
    def perfectAccuracy (self):
        global score
        score = score*0;  
    """ Scoring for Execution Time for choice precision"""
    @Rule(Fact("p") and Fact(executionTimeScore = 10))
    def exeTime10 (self):
        global score
        score = score*10
    @Rule(Fact("p") and Fact(executionTimeScore = 9))
    def exeTime9 (self):
        global score
        score = score*9
    @Rule(Fact("p") and Fact(executionTimeScore = 8))
    def exeTime8 (self):
        global score
        score = score*8
    @Rule(Fact("p") and Fact(executionTimeScore = 7))
    def exeTime7 (self):
        global score
        score = score*7
    @Rule(Fact("p") and Fact(executionTimeScore = 6))
    def exeTime6 (self):
        global score
        score = score*6
    @Rule(Fact("p") and Fact(executionTimeScore = 5))
    def exeTime5 (self):
        global score
        score = score*5
    @Rule(Fact("p") and Fact(executionTimeScore = 4))
    def exeTime4 (self):
        global score
        score = score*4
    @Rule(Fact("p") and Fact(executionTimeScore = 3))
    def exeTime3 (self):
        global score
        score = score*3
    @Rule(Fact("p") and Fact(executionTimeScore = 2))
    def exeTime2 (self):
        global score
        score = score*2
    @Rule(Fact("p") and Fact(executionTimeScore = 1))
    def exeTime1 (self):
        global score
        score = score*1
    @Rule(Fact("p") and Fact(executionTimeScore = 0))
    def exeTime0 (self):
        global score
        score = score*0
    """ Scoring for Execution Time for choice speed"""
    @Rule(Fact("s") and Fact(executionTimeScore = 10))
    def exeTimespeed10 (self):
        global score
        score = score*100
    @Rule(Fact("s") and Fact(executionTimeScore = 9))
    def exeTimespeed9 (self):
        global score
        score = score*90
    @Rule(Fact("s") and Fact(executionTimeScore = 8))
    def exeTimespeed8 (self):
        global score
        score = score*80
    @Rule(Fact("s") and Fact(executionTimeScore = 7))
    def exeTimespeed7 (self):
        global score
        score = score*70
    @Rule(Fact("s") and Fact(executionTimeScore = 6))
    def exeTimespeed6 (self):
        global score
        score = score*60
    @Rule(Fact("s") and Fact(executionTimeScore = 5))
    def exeTimespeed5 (self):
        global score
        score = score*50
    @Rule(Fact("s") and Fact(executionTimeScore = 4))
    def exeTimespeed4 (self):
        global score
        score = score*40
    @Rule(Fact("s") and Fact(executionTimeScore = 3))
    def exeTimespeed3 (self):
        global score
        score = score*30
    @Rule(Fact("s") and Fact(executionTimeScore = 2))
    def exeTimespeed2 (self):
        global score
        score = score*20
    @Rule(Fact("s") and Fact(executionTimeScore = 1))
    def exeTimespeed1 (self):
        global score
        score = score*10
    @Rule(Fact("s") and Fact(executionTimeScore = 0))
    def exeTimespeed0 (self):
        global score
        score = score*0
    
    """General Scoring, same for both choices"""
    """ Scoring for Specificity"""
    @Rule(Fact(specificity = 'specific'))
    def specificenough(self):
        global score
        score = score +100
    @Rule(Fact(specificity = 'barely specific'))
    def barelySpecifice(self):
        global score
        score = score +50
    @Rule(Fact(specificity = 'specificity worst than random'))
    def notSpecific(self):
        pass 
        
    
    """ Scoring for Sensitivity"""
    @Rule(Fact(specificity = 'sensitive'))
    def specificenough(self):
        global score
        score = score +100
    @Rule(Fact(specificity = 'barely sensitive'))
    def barelySpecifice(self):
        global score
        score = score +50
    @Rule(Fact(specificity = 'sensitivy worst than random'))
    def notSpecific(self):
        pass 