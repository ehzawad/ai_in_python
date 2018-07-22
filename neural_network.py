import random
import math


class ForwardPropagation:
    def __init__(self):
        # Inputs
        self.input1 = 0.05
        self.input2 = 0.10

        # Outputs
        self.output1 = 0.80
        self.output2 = 0.99

        # bias
        self.bias1 = 0.35
        self.bias2 = 0.60

        # self.weight = list(range(9))
        self.weight = [.15, .20, .25, .30, .40, .45, .50, .55]

        # Hidden Layer
        self.hidden1 = 0.0
        self.hidden2 = 0.0

        self.tempo1 = 0.0
        self.tempo2 = 0.0

        self.error1 = 0.0
        self.error2 = 0.0

        self.input1Lowest = 0.0
        self.input2Lowest = 0.0

        self.lowestError = 1
        self.randomValue = random.random()

    def calculateNet(self, i1, i2, w1, w2, b):
        return (w1*i1)+(w2*i2)+(b*1)

    def calculateOutput(self, val):
        return (1/(1+math.exp(-val)))

    def calculateError(self, targetO, output):
        return (0.5 * ((targetO - output) * (targetO - output)))

    def forwardPropagation(self):
        # self.inputEdgeWeight()

        for i in range(100):
            self.forwardPassPropagation()

        print("for the value of i1 & i2 :")
        print(str(self.input1Lowest) + "," + str(self.input2Lowest))

    def forwardPassPropagation(self):
        self.input1 = random.random()
        self.input2 = random.random()
        print("input1: " + str(self.input1) + "input2: " + str(self.input2))
        self.hidden1 = self.calculateNet(self.input1, self.input2, self.weight[0], self.weight[1], self.bias1)
        self.hidden1 = self.calculateOutput(self.hidden1)
        self.hidden2 = self.calculateNet(self.input1, self.input2, self.weight[2], self.weight[3], self.bias1)
        self.hidden2 = self.calculateOutput(self.hidden2)

        self.tempo1 = self.calculateNet(self.hidden1, self.hidden2, self.weight[4], self.weight[5], self.bias2)
        self.tempo1 = self.calculateOutput(self.tempo1)
        self.tempo2 = self.calculateNet(self.hidden1, self.hidden2, self.weight[6], self.weight[7], self.bias2)
        self.tempo2 = self.calculateOutput(self.tempo2)

        # error
        self.error1 = self.calculateError(self.output1, self.tempo1)
        print("error1: " + str(self.error1))
        self.error2 = self.calculateError(self.output2, self.tempo2)
        print("error2: " + str(self.error2))

        self.Error = self.error1 + self.error2

        if self.Error < self.lowestError:
            self.input1Lowest = self.input1
            self.input2Lowest = self.input2

        print("Total error: " + str(self.error1 + self.error2))


demo = ForwardPropagation()
demo.forwardPropagation()
