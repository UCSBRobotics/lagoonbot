from random import random
from random import seed
import numpy as np

def init_net(n_inputs, n_hidden, n_output):
    network = []
    hidden = [{"weights" : [random() for j in range(n_inputs+1)]} for i in range(n_hidden)]
    network.append(hidden)
    output = [{"weights" : [random() for j in range(n_hidden+1)]} for i in range(n_output)]
    network.append(output)
    return network

#test = init_net(2, 3, 2)
#print (test)
def activation(input_x):
    return 1 / (1 + (np.exp(-input_x)))

print (activation(1))

def lin(weights, inputs):
    pass