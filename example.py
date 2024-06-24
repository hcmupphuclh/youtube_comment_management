from abc import ABC, abstractmethod

class Agent(ABC):
    
    def __init__(self) -> None:
        self._observation = None
        self.prediction = None
        
    def getObservation(self) -> str:
        return self._observation
    
    def setObservation(self, observation: str):
        self._observation = observation
    
    def getPrediction(self) -> str:
        return self._prediction
    
    def setPrediction(self, prediction: str):
        self._prediction = prediction
        
    observation = property(getObservation, setObservation, fdel=None, doc=None)
    prediction = property(getPrediction, setPrediction, fdel=None, doc=None)
    
    @abstractmethod
    def perceive_world(self):
        pass

class Dumb_agent(Agent):
    
    def perceive_world(self):
        print('I see %s' % self.observation)
        if self.prediction is not None:
            print('I am too dumb to make a prediction, but I tried anyway')

class Clever_Agent(Agent):
        
    def perceive_world(self):
        print('I see %s' % self.observation)
        print('I think I am going to see %s happen next' % self.prediction)
        
dumb_agent = Dumb_agent()
dumb_agent.perceive_world

clever_agent = Clever_Agent()
clever_agent.perceive_world