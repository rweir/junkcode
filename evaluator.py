class Literal(object):
    def __init__(self, value):
        self.value = value
    def evaluate(self):
        return self.value

class Addition(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def evaluate(self):
        return self.x.evaluate() + self.y.evaluate()

class Multiplication(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def evaluate(self):
        return self.x.evaluate() * self.y.evaluate()

def evaluate_expression(exp):
    return exp.evaluate()

exp = (Addition(Literal(10), Multiplication(Literal(5), Literal(4))))
print evaluate_expression(exp)
