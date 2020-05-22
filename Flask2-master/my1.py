print(__name__)

def add(a, b):
    return a+b
def sub(a,b):
    return a-b

class BusinessCard:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("--------------------")
        print("Name: ", self.name)

class Woman:
    def __init__(self, weight,height,iq):
        self.weight = weight
        self.height = height
        self.iq = iq

    def eat(self):
        self.weight+=5

    def study(self):
        self.iq+=1

    def sleep(self):
        self.height+=1

    def print_her_info(self):
        print("--------------------")
        print("weight: ", self.weight)
        print("height: ", self.height)
        print("iq: ", self.iq)