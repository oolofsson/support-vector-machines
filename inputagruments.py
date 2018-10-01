import argparse
import sys

def readInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="sets the \"Slack\" variable", type=int)
    parser.add_argument("-n",  help="The number of datapoints generated", type=int)
    parser.add_argument("-k", help="Specifies kerel function to use (linear, polynomal, radius)", type=str)
    parser.add_argument("-d",  help="Specifies which dataset to use (smallClusters, largecluster, oskars)", type=str)
    args = parser.parse_args()
    if args.c is None:
        print("You must specify a slack variable using \"-c\". \nExample: python3 lab2.py -c 10")
        sys.exit(0)
    if args.n is None:
        print("You must specify the the number of datapoints to be generated using \"-n\". \nExample: python3 lab2.py -c 10 -n 40")
        sys.exit(0)
    if args.k is None:
        print("You must specify the kernel function to be used by using \"-k\". \nExample: python3 lab2.py -c 10 -n 40 -k linear")
        sys.exit(0)
    if args.d is None:
        print("You must specify which dataset to be used by using \"-d\". \nExample: python3 lab2.py -c 10 -n 40 -k linear -d smallClusters")
        sys.exit(0)
    return args.c, args.n, args.k, args.d

'''def main ():
    c, n, k, d = readInput()
    print (k)

main()
'''
