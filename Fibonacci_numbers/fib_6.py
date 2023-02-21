import matplotlib.pyplot as plt
import time
import pandas as pd
import sys

sys.setrecursionlimit(50000)
fibon_num = []
x = []
y = []
fib_low = [5,7,10,12,15,17,20]
fib_high = [501,631,794,1000,1259,1585,1995,2512,3162,3981,5012,6310,7943,10000,12589,15849]
def multiply(a, b):
     
    mul = [[0 for x in range(3)]
              for y in range(3)]
    for i in range(3):
        for j in range(3):
            mul[i][j] = 0
            for k in range(3):
                mul[i][j] += a[i][k] * b[k][j]
 

    for i in range(3):
        for j in range(3):
            a[i][j] = mul[i][j]; 
    return a

def power(F, n):
 
    M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
 
    if (n == 1):
        return F[0][0] + F[0][1]
 
    power(F, int(n / 2))
 
    F = multiply(F, F)
 
    if (n % 2 != 0):
        F = multiply(F, M)

    return F[0][0] + F[0][1] 
 

def findNthTerm(n):
    F = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
 
    return power(F, n - 2)

for row in fib_high:
    print('{:^7}'.format(row),end='')
    
print('')

for i in range(16):
    start = time.time()
    fibon_num.append(findNthTerm(fib_high[i]))
    end = time.time()
    x.append(fib_high[i])
    y.append(end-start)
    print('{:^7.4f}'.format(end-start),end='')
    plt.plot(x,y)
    plt.draw()


plt.xlabel('x - n-th Fibonacci number')
plt.ylabel('y - time spent (s)')
plt.show()
