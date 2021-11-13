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
    return 1.0 / (1.0 + (np.exp(-input_x)))

#print (activation(1))

def lin(weights, inputs):
    sum = 0
    for j in range(len(inputs) - 1):
        sum += weights[j] * inputs[j]
    
    sum += weights[-1]
    return sum

def forward_prop(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = lin(neuron['weights'], inputs)
            neuron['output'] = activation(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

test = init_net(3, 2, 2)
row = [1, 0, None]
output = forward_prop(test, row)
print (output)