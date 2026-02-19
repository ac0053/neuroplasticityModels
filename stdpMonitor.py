import scipy
import numpy as np
import self
import SNS_json
from sns_toolbox.connections import NonSpikingSynapse
import sns_toolbox.networks
import matplotlib.pyplot as plt
from sns_toolbox.neurons import NonSpikingNeuron
import time
import seaborn as sns

class stdpMonitor(self, jsonFileSave, modelFile):
    def __init__(self):
        #simulation time initialization
        self.dt = 1 #step
        self.tMax = 2e3 #2000 ms
        self.t = np.linspace(0, self.tMax, self.dt)
        self.numsteps = len(self.t)

    def temporal_encoding(modelFile):


    def monitor(self, jsonFileSave, modelFile):
        # save and load model parameters (i.e. connections, output neurons,...)
        dataOut = {}
        for i in range(self.numsteps): #simulate response
            dataOut[i,:] = modelFile.model() #assumes that model has been compiled already in NN script




