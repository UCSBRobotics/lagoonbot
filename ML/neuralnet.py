from random import random
from random import seed
import numpy as np

def init_weights(n_inputs, n_hidden, n_output):
	# input -> hidden weights
	hidden = np.random.rand(n_hidden, n_inputs + 1)
	# hidden -> output weights
	output = np.random.rand(n_output, n_hidden + 1)
	return [hidden, output]


def activation(input_x):
	return 1 / (1 + (np.exp(-input_x)))

def lin(weights, inputs):
	if len(weights) != len(inputs) + 1:
		print('eat shit')
		return

	sum = 0
	for j in range(len(inputs)):
		sum += weights[j] * inputs[j]
	
	# bias
	sum += weights[-1]
	return sum

def forward_pass(network, outputs, row):
	inputs = row
	for i in range(len(network)):
		layer = network[i]
		new_inputs = []
		for j in range(len(layer)):
			neuron = layer[j]
			activation1 = lin(neuron, inputs)
			outputs[i][j]  = activation(activation1)
			new_inputs.append(outputs[i][j])
		inputs = new_inputs
	return inputs

shape = (3, 2, 2)
network = init_weights(shape[0], shape[1], shape[2])
outputs = np.zeros(shape)
inputs = [1, 0, 1]
output = forward_pass(network, outputs, inputs)
print (output)
