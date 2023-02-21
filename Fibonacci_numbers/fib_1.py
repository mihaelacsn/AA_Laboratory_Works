import matplotlib.pyplot as plt
import time
import pandas as pd

fibon_num = []
x = []
y = []
fib_low = [5,7,10,12,15,17,20]
fib_high = [501,631,794,1000,1259,1585,1995,2512,3162,3981,5012,6310,7943,10000,12589,15849]

def fib_recursion(n):
    if n <= 1:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)

    
for row in fib_low:
    print('{:^10}'.format(row),end='')
    
print('')

for i in range(7):
    start = time.time()
    fibon_num.append(fib_recursion(fib_low[i]))
    end = time.time()
    x.append(fib_low[i])
    y.append(end-start)
    print('{:^10}'.format(end-start),end='')
    plt.plot(x,y)
    plt.draw()


plt.xlabel('x - n-th Fibonacci number')
plt.ylabel('y - time spent (s)')
plt.show()
