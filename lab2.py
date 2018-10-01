import numpy , random , math
from scipy.optimize import minimize
from scipy.spatial import distance
import matplotlib.pyplot as plt

import dataset as dataset
import inputagruments as ioargs

def zerofun(a):
    return numpy.dot(a, targets)

def precalculate(inputs, kernel, targets):
    for i in range(0, len(precalculated)):
        for j in range(0, len(precalculated[0])):
            precalculated[i][j] = targets[i] * targets[j] * kernel(inputs[i], inputs[j])

def radial_basis_function_kernel(x, y):
    global SIGMA
    return math.exp(-((distance.euclidean(x, y)**2)/(2*SIGMA*SIGMA)))

def polynomial_kernel(x, y):
    global polyGrade
    return (numpy.dot(numpy.transpose(x), y) + 1)**polyGrade

def linear_kernel(x, y):
    return numpy.dot(numpy.transpose(x), y)


def objective(a):
    sum1 = 0.0
    sum2 = 0.0
    for i in range(0, len(precalculated)):
        sum2 = sum2 + a[i]
        for j in range(0, len(precalculated[0])):
            sum1 = sum1 + (a[i] * a[j] * precalculated[i][j])
    return 0.5*sum1 - sum2

def calculateB(sv, target, nA, nInputs, nTargets, kernel):
    sum = 0.0
    for i in range(0, len(nA)):
        sum += nA[i] * nTargets[i] * kernel(sv, nInputs[i])
    return sum - target;

def indicator(x, y, nA, nInputs, nTargets, kernel):
    sum = 0.0
    b = calculateB(nInputs[1], nTargets[1], nA, nInputs, nTargets, kernel)
    for i in range(0, len(nA)):
        sum += nA[i] * nTargets[i] * kernel([x, y], nInputs[i])

    return sum - b

def plot(nA, nInputs, nTargets, kernel):
    xgrid = numpy.linspace(-5, 5)
    ygrid = numpy.linspace(-4, 4)

    # check which kernel we are using
    if kernel == "linear":
        grid = numpy.array([[indicator(x, y, nA, nInputs, nTargets, linear_kernel)
                        for x in xgrid]
                        for y in ygrid])
    elif kernel == "polynomal":
        grid = numpy.array([[indicator(x, y, nA, nInputs, nTargets, polynomial_kernel)
                        for x in xgrid]
                        for y in ygrid])
    else:
        grid = numpy.array([[indicator(x, y, nA, nInputs, nTargets, radial_basis_function_kernel)
                        for x in xgrid]
                        for y in ygrid])

    plt.contour(xgrid, ygrid, grid, (-1.0, 0.0, 1.0),
                colors=('red', 'black', 'blue'),
                linewidths=(1, 3, 1))

    plt.show()

# GLOBALS
targets = []
outofbounds = []
N = 40
start = numpy.zeros(N)
i, j = N, N;
precalculated = [[0 for l in range(0, j)] for k in range(0, i)]
C = 100
B = [(0, C) for b in range(N)] # bounds
XC = {'type':'eq', 'fun': zerofun} # constraints
polyGrade = 2
SIGMA = 5

def updateB(n):
    global B
    global precalculated
    global start
    B = [(0, C) for b in range(n)] # bounds
    precalculated = [[0 for l in range(0, n)] for k in range(0, n)]
    start = numpy.zeros(N)

def extract_nonzeroes(a, inputs, targets):
  nA = []
  nInputs = []
  nTargets = []
  for i in range(0, len(a)):
      if a[i] > 0.00001 or a[i] < -0.00001:
        nA.append(a[i])
        nInputs.append(inputs[i])
        nTargets.append(targets[i])
  return nA, nInputs, nTargets

def main():
    inC, inN, inK, inD, inP, inS = ioargs.readInput()

    #   overwrite existing global variables
    global N
    global C
    global i, j
    N = inN
    C = inC
    i, j = N, N
    updateB(N)
    global targets
    inputs, targets, classA, classB = dataset.generateData(inN, inD)
    plt.plot([p[0] for p in classA], [p[1] for p in classA],'b.')
    plt.plot([p[0] for p in classB], [p[1] for p in classB],'r.')

    if inK == "linear":
        precalculate(inputs, linear_kernel, targets)
    elif inK == "polynomal":
        precalculate(inputs, polynomial_kernel, targets)
    else:
        precalculate(inputs, radial_basis_function_kernel, targets)

    ret = minimize(objective, start, bounds=B, constraints=XC)

    a = ret['x']
    success = ret['success']
    if success == True:
        print ("Optimal solution found")
    else:
        print ("No optimal solution could be found")
    nA, nInputs, nTargets = extract_nonzeroes(a, inputs, targets)
    plot(nA, nInputs, nTargets, inK)

main()
