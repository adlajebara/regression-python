from numpy import *
import sys
import matplotlib.pyplot as plt

def main():
    measurements = loadtxt(sys.argv[1])
    data = transpose(measurements)
    X = data[0]
    Y = data[1]

    n = int(sys.argv[2])
    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    step = int(max(X) - min(X)/0.2)
    X2 = linspace(min(X),max(X),step).tolist()
    Y2 = [poly(a,x) for x in X2]

    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()

def poly(a,x):
    a = flip(a)
    res = polyval(a,x)
    return res

def powers(list, n1, n2):
    #create a new empty matrix
    res = []
    for i in range(len(list)):
        row = []*len(list)
        res.append(row)

    if len(list) == 0:
        return []
    else:
        for n in range(n1, n2+1):
            for i in range(len(list)):
                res[i] += [(float(list[i])**n)]
    return array(res)

main()
