class Calculator:
    def __init__(self):
        self.initial = 0

    
    def add(self, number):
        self.initial += number
        return self.initial


    def subtract(self, number):
        self.initial -= number
        return self.initial

    
    def show(self):
        print(self.initial)


calc = Calculator()
calc.add(5)
calc.add(3)
calc.subtract(2)
calc.show()