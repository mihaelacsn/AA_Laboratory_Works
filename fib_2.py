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


def fib_tail_recursion (n, i = 0, crr = 0, next = 1):
    if n == i:
        return crr
    
    else:
        return fib_tail_recursion(n, i+1, next, crr + next)


    
for row in fib_high:
    print('{:^7}'.format(row),end='')
    
print('')

for i in range(16):
    start = time.time()
    fibon_num.append(fib_tail_recursion(fib_high[i]))
    end = time.time()
    x.append(fib_high[i])
    y.append(end-start)
    print('{:^7.4f}'.format(end-start),end='')
    plt.plot(x,y)
    plt.draw()


plt.xlabel('x - n-th Fibonacci number')
plt.ylabel('y - time spent (s)')
plt.show()