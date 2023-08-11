class A():
    def __init__(self):
        self.bop = 1
    def myFunc(self, input):
        return input * 2

instance1 = A()

print(instance1.myFunc(2))

def newFunc(a):
    return a * 5

instance1.myFunc2 = newFunc

print(instance1.myFunc2(2))

def newFunc(a):
    return a * 3


print(instance1.myFunc2(2))
