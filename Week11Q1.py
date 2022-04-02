class calculator:

    def __init__(self):
        self.currentInput = 0

    def adder(self, input1, input2):
        self.currentInput = (input1 + input2)
        print(self.currentInput)
        return self.currentInput

    def subtractor(self, input1, input2):
        self.currentInput = (input1 - input2)
        print(self.currentInput)
        return self.currentInput

    def multiplier(self, input1, input2):
        self.currentInput = (input1 * input2)
        print(self.currentInput)
        return self.currentInput

    def divider(self, input1, input2):
        self.currentInput = (input1 / input2)
        print(self.currentInput)
        return self.currentInput

    def clear(self):
        if(self.currentInput > 0 or self.currentInput < 0):
            self.currentInput = 0
        print(self.currentInput)

calculator = calculator()
calculator.adder(2,3)
calculator.multiplier(4,7)