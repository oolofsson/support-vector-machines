import numpy , random , math
from scipy.optimize import minimize
from scipy.spatial import distance
import matplotlib.pyplot as plt

import dataset as dataset

def zerofun(a):
    return numpy.dot(a, targets)

def precalculate(inputs, kernel, targets):
    for i in range(0, len(precalculated)):
        for j in range(0, len(precalculated[0])):
            precalculated[i][j] = targets[i] * targets[j] * kernel(inputs[i], inputs[j])

def radial_basis_function_kernel(x, y, sigma = 5):
    return math.exp(-((distance.euclidean(x, y)**2)/(2*sigma*sigma)))

def polynomial_kernel(x, y, p = 3):
    return (numpy.dot(numpy.transpose(x), y) + 1)**p

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

def indicator(x, y, nA, nTargets, nInputs, kernel):
    sum = 0.0
    sumB = 0.0

    for i in range(0, len(nA)):
        sum += nA[i] * nTargets[i] * kernel([x, y], nInputs[i])
        #sumB += nA[i] * nTargets[i] * kernel([x, y], nInputs[i]) - nTargets[x*y]

    return sum - sumB

def plot(nA, nInputs, nTargets):
    xgrid = numpy.linspace(-5, 5)
    ygrid = numpy.linspace(-4, 4)
    grid = numpy.array([[indicator(x, y, nA, nTargets, nInputs, radial_basis_function_kernel)
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

    global targets
    inputs, targets, classA, classB = dataset.generateData(N)

    precalculate(inputs, radial_basis_function_kernel, targets)
    ret = minimize(objective, start, bounds=B, constraints=XC)

    a = ret['x']
    success = ret['success']
    print (success)
    nA, nInputs, nTargets = extract_nonzeroes(a, inputs, targets)
    dataset.printData(classA, classB)
    plot(nA, nInputs, nTargets)

main()
