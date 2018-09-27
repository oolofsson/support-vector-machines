import numpy , random , math
from scipy.optimize import minimize
from scipy.spatial import distance
import matplotlib.pyplot as plt

def zerofun(a):
    for i in range(0, len(a)):
        if a[i] > C or a[i] < 0:
            print("out of bounds in zerofun")
    return numpy.dot(a, t)

def precalculate(x, kernel):
    for i in range(0, len(precalculated)):
        for j in range(0, len(precalculated[0])):
            precalculated[i][j] = t[i]*t[j]*kernel(x, x)

def radial_basis_function_kernel(x, y, sigma = 1):
    return math.exp(-((distance.euclidean(x, y)**2)/(2*sigma*sigma)))

def polynomial_kernel(x, y, p = 3):
    return (numpy.dot(numpy.transpose(x), y) + 1)**p

def linear_kernel(x, y):
    return numpy.dot(numpy.transpose(x), y)

def objective(a):
    #0.5*
    sum1 = 0
    sum2 = 0
    for i in range(0, len(precalculated)):
        sum2 += a[i]
        for j in range(0, len(precalculated[0])):
            sum1 += a[i]*a[j]*precalculated[i][j]

    return 0.5*sum1 - sum2

def offset_bias_hyperplane(s, x, kernel):
    sum = 0
    for i in range(0, len(a)):
        sum = sum + a[i]*t[i]*kernel(s, x[i]) - t[s]
    return sum

def indicator(s, x, kernel):
    sum = 0
    for i in range(0, len(a)):
        print(i)
        print(len(a))
        #print(len(t))
        print(len(x))
        sum = sum + a[i]*t[i]*kernel(s, x[i])
    return sum - offset_bias_hyperplane(s, x, kernel)

def plot(x):
    xgrid = numpy.linspace(-5, 5)
    ygrid = numpy.linspace(-4, 4)
    grid = numpy.array([[indicator(x, y, linear_kernel)
                        for x in xgrid ]
                        for y in ygrid])

    plt.contour(xgrid, ygrid, grid, (-1.0, 0.0, 1.0),
                colors=('red', 'black', 'blue'),
                linewidths=(1, 3, 1))

# GLOBALS
N = 10
start = numpy.zeros(N)
i, j = 5, 5;
precalculated = [[0 for l in range(0, j)] for k in range(0, i)]
C = 1
B = [(0, C) for b in range(N)] # bounds
XC = {'type':'eq', 'fun':zerofun} # constraints
t = [1, -1, 1, 1, -1, -1, 1, 1, -1, 1]
a = [1, 4, 3, 3, 7, 9, 22, 1, 23, 10]

def main():

    precalculate(a, radial_basis_function_kernel)
    ret = minimize(objective, start, bounds=B, constraints=XC)
    alphaX = ret['x']
    alphaSuccess = ret['success']
    print("alpha x :", alphaX)
    print("alpha success :", alphaSuccess)
    '''
    print(vector)
    print(linear_kernel([3, 0,4, 2], [2, 0 ,1, 9]))
    print("pol kern: ", polynomial_kernel([3, 0,4, 2], [2, 0 ,1, 9], 2))
    #print(objective([0,7,11], [0, 83, 2]))
    print("rbf kern: ", radial_basis_function_kernel([3, 0, 4, 2], [2, 0 ,1, 9], 1))
    print("zerofun: ", zerofun([0,2,2], [1, -1 , 1], 10))

    print("before: ", precalculated)
    precalculate([1, -1, 1, 1, 1], [4, 3, 7, 8, 5], linear_kernel)
    print("william: ", precalculated)

    print(objective([1, 4, 3, 3, 7]))
    '''

    nonzero = [i for i in alphaX if not 0]
    print("alpha: ", alphaX)
    print("nonzero: ", nonzero)

    plot()

main()
