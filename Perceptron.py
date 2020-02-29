import random

class Perceptron:
    def __init__(self, num_of_inputs):
        self.num_of_inputs = num_of_inputs
        self.weights = []
        self.learning_rate = 0.1
        self.__generate_n_random_values()


    def __generate_n_random_values(self):
        for _ in range(self.num_of_inputs):
            weight = random.uniform(-1, 1)
            self.weights.append(weight)  


    def __set_inputs(self, *inputs):
        if len(inputs) != self.num_of_inputs:
            print("Error: number of inputs is not as declared")
        else:
            self.inputs = inputs

    
    def __weighted_sum(self):
        self._weighted_sum = 0
        for i in range(self.num_of_inputs):
            self._weighted_sum = self._weighted_sum + self.inputs[i] * self.weights[i]

    def __sign(self):
        if self._weighted_sum>=0:
            sign = 1
        else:
            sign = -1
        return sign


    def train(self, *inputs, target):
        self.output = self.get_output(*inputs)
        error = target - self.output       
        for i in range(len(self.weights)):
            delta_weight = error * self.inputs[i]
            self.weights[i] = self.weights[i] + delta_weight * self.learning_rate

    def get_output(self, *inputs):
        self.__set_inputs(*inputs)
        self.__weighted_sum()
        self.output = self.__sign()
        return self.output

    def get_weights(self):
        return self.weights
        
