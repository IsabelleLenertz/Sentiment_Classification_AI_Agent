from random import choice
from pyknow import *
from kb import *

engine = RobotCrossStreet()
engine.reset()
engine.declare(Light(color=choice(['green', 'yellow', 'blinking-yellow', 'red'])))
engine.run()
