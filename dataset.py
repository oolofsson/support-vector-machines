import numpy , random , math
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# generate a basic dataset
def basicDataset():
    classA = numpy.concatenate((numpy.random.randn(10,2)*0.2+[ 1.5 , 0.5 ], numpy.random.randn(10,2)*0.2+[-1.5,0.5]))
    classB = numpy.random.randn(20, 2) * 0.2 + [0.0, -0.5]
    return classA, classB

'''
    We can add more complexe datasets here if we need to
'''

def generateData():
    numpy.random.seed(100)
    classA, classB = basicDataset()
    inputs = numpy.concatenate((classA, classB))
    targets = numpy.concatenate((numpy.ones(classA.shape[0]), - numpy.ones(classB.shape[0])))
    N = inputs.shape[0]
    permute = list(range(N))
    random.shuffle(permute)
    inputs = inputs[permute, :]
    targets = targets[permute]
    print(permute)
    printData(classA, classB)

def printData(classA, classB):
    plt.plot([p[0] for p in classA], [p[1] for p in classA],'b.')
    plt.plot([p[0] for p in classB], [p[1] for p in classB],'r.')
    plt.axis('equal')
    plt.show()

def main():
    generateData()

main()
