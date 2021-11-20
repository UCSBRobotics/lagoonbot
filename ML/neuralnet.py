from random import random
from random import seed
import numpy as np

def init_weights(n_inputs, n_hidden, n_output):
	# input -> hidden weights
	hidden = np.random.rand(n_hidden, n_inputs + 1)
	# hidden -> output weights
	output = np.random.rand(n_output, n_hidden + 1)
	return np.array([hidden, output])


def activation(input_x):
	return 1 / (1 + (np.exp(-input_x)))

def lin(weights, inputs):
	if (len(weights) != len(inputs) + 1)
		print('eat shit')
		return

	sum = 0
	for j in range(len(inputs)):
		sum += weights[j] * inputs[j]
	
	sum += weights[-1]
	return sum

def forward_prop(network, row):
	print(network)
	inputs = row
	counter = 0
	for layer in network:
		print('layer type:', type(layer))
		print('layer dtype:', layer.dtype)
		new_inputs = []
		for neuron in layer:
			print('neuron type:', type(neuron))
			print('iter:', counter)
			print('wlen:', len(neuron['weights']))
			activation1 = lin(neuron['weights'], inputs)
			neuron['output'] = activation(activation1)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
		counter += 1
	return inputs

'''
test = init_net(3, 2, 2)
row = [1, 0, 1]
output = forward_prop(test, row)
print (output)
'''
