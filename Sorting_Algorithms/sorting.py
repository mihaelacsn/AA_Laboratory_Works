import random
from numpy import random
import matplotlib.pyplot as plt
import time

#Sorting:
#quickSort:
data1 = random.randint(100, size=(10))
data2 = random.randint(1000, size=(100))
data3 = random.randint(100000, size=(1000))
x = []
y = []
print("Initial array for sorting:")
print(data1)
print(data2)
print(data3)
def partition(arr, left, right):
  
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[right]) = (arr[right], arr[i + 1])
    return i + 1

def quickSort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quickSort(arr, left, pi - 1)
        quickSort(arr, pi + 1, right)

size1 = len(data1)
size2 = len(data2)
size3 = len(data3)


#mergeSort method:
def mergeSort(array):
    if len(array) > 1:

        half = len(array)//2
        l1 = array[:half]
        l2 = array[half:]

        mergeSort(l1)
        mergeSort(l2)

        i = j = k = 0

        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                array[k] = l1[i]
                i += 1
            else:
                array[k] = l2[j]
                j += 1
            k += 1

        while i < len(l1):
            array[k] = l1[i]
            i += 1
            k += 1

        while j < len(l2):
            array[k] = l2[j]
            j += 1
            k += 1
#heapSort:
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#bubbleSort:
def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

print("What sorting method you want to try?")
choice = input()

#Menu for sorting:
match choice:
        case "quickSort":
            start = time.time()
            quickSort(data1, 0, size1 - 1)
            end = time.time()
            x.append(10)
            y.append(end-start)
            start = time.time()
            quickSort(data2, 0, size2 - 1)
            end = time.time()
            x.append(100)
            y.append(end-start)
            start = time.time()
            quickSort(data3, 0, size3 - 1)
            end = time.time()
            x.append(1000)
            y.append(end-start)
        case "mergeSort":
            start = time.time()
            mergeSort(data1)
            end = time.time()
            x.append(10)
            y.append(end-start)
            start = time.time()
            mergeSort(data2)
            end = time.time()
            x.append(100)
            y.append(end-start)
            start = time.time()
            mergeSort(data3)
            end = time.time()
            x.append(1000)
            y.append(end-start)
        case "heapSort":
            start = time.time()
            heapSort(data1)
            end = time.time()
            x.append(10)
            y.append(end-start)
            start = time.time()
            heapSort(data2)
            end = time.time()
            x.append(100)
            y.append(end-start)
            start = time.time()
            heapSort(data3)
            end = time.time()
            x.append(1000)
            y.append(end-start)
        case "bubbleSort":
            start = time.time()
            bubbleSort(data1)
            end = time.time()
            x.append(10)
            y.append(end-start)
            start = time.time()
            bubbleSort(data2)
            end = time.time()
            x.append(100)
            y.append(end-start)
            start = time.time()
            bubbleSort(data3)
            end = time.time()
            x.append(1000)
            y.append(end-start)
                
        case _ :
            print("I don't know this method for sorting:")

            
plt.plot(x,y)
plt.draw()
plt.xlabel('x - number of elements in the array')
plt.ylabel('y - time spent for sorting (s)')
plt.show()
print('The final, sorted array:')
print(data1)
print(data2)
print(data3)
