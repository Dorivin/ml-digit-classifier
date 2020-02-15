import random

class Perceptron:
    def __init__(self):
        self.weights = []

    def set_inputs(self, *inputs):
        self.list_of_inputs = inputs
        self.num_of_inputs = len(self.list_of_inputs)

    def __generate_n_random_values(self):
        for _ in range(self.num_of_inputs):
            weight = random.uniform(-1, 1)
            self.weights.append(weight)  

    def __weighted_sum(self):
        self._weighted_sum = 0
        for i in range(self.num_of_inputs):
            self._weighted_sum = self._weighted_sum + self.list_of_inputs[i] * self.weights[i]

    def __sign(self):
        if self._weighted_sum>=0:
            sign = 1
        else:
            sign = -1
        return sign

    def get_output(self):        
        self.__generate_n_random_values()
        self.__weighted_sum()
        self.output = self.__sign()
        return self.output

    def get_weights(self):
        return self.weights
        
