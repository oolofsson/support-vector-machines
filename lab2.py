import numpy , random , math
from scipy.optimize import minimize
from scipy.spatial import distance
import matplotlib.pyplot as plt


N = 27

vector = numpy.zeros(N)

i, j = 5, 5;
precalculated = [[0 for l in range(0, j)] for k in range(0, i)]

C = 1

bounds=[(0, C) for b in range(N)]

#constraint={'type':'eq', 'fun':zerofun}

#K(⃗x, ⃗y ) = ⃗x T · ⃗y

#P i,j = t i t j K(⃗x i , ⃗x j )

#pij_array = pij(0, 0, 0, 0, 0)

def precalculate(t, x, kernel):
    for i in range(0, len(precalculated)):
        for j in range(0, len(precalculated[0])):
            precalculated[i][j] = t[i]*t[j]*kernel(x, x)


def pij(t, i, j, x, y):
    t[i]*t[j]*linear_kernel(x, y)

#K(⃗x, ⃗y ) = (⃗x T · ⃗y + 1) p

def radial_basis_function_kernel(x, y, sigma = 1):
    return math.exp(-((distance.euclidean(x, y)**2)/(2*sigma*sigma)))

def polynomial_kernel(x, y, p = 3):
    return (numpy.dot(numpy.transpose(x), y) + 1)**p

def linear_kernel(x, y):
    return numpy.dot(numpy.transpose(x), y)


#0.5 * ∑ ∑ α i α j t i t j K(⃗x i , ⃗x j ) − ∑ α i

def objective(a):
    #0.5*
    sum1 = 0
    sum2 = 0
    for i in range(0, len(precalculated)):
        sum2 += a[i]
        for j in range(0, len(precalculated[0])):
            sum1 += a[i]*a[j]*precalculated[i][j]

    return 0.5*sum1 - sum2

    #numpy.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>)[source]

def zerofun(a, t, C):
    for i in range(0, len(a)):
        if a[i] > C or a[i] < 0:
            print("out of bounds in zerofun")
            return False
    if(numpy.dot(a,t) != 0):
        print("dot product not zero")
        return False
    else:
        return True



def main():
   #ret = minimize (objective, start, bounds=B, constraints=XC )
   #alpha = ret['x']
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


main()
