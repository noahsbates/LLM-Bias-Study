import os

#gets relative directory
def getRelDir():
    a = os.path.realpath(__file__)
    b = os.path.dirname(a)
    return b