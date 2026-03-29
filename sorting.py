import time
import random

def time_taken(func,*args):
    start = time.perf_counter()
    res = func(*args)
    end = time.perf_counter()
    print(f'{func.__name__} : ({end-start} s)')

class sort:
    def bubbleSort(a: list[int]) -> list[int]:
        l = len(a)
        for i in range(l-1):
            swaps = 0
            for j in range(l-1-i):
                if a[j]>a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
                    swaps+=1
            if swaps == 0:
                return a
        return a

    def insertionSort(a: list[int]) -> list[int]:
        l = len(a)
        for i in range(1,l):
            j = i
            while (j-1)>=0 and a[j]<a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
                j-=1
        return a

    def selectionSort(a: list[int]) -> list[int]:
        l = len(a)
        for i in range(l-1):
            minInd = i
            for j in range(i,l):
                if a[j] < a[minInd]:
                    minInd = j
            if i != minInd:
                a[i],a[minInd] = a[minInd],a[i]
        return a

    def partition(a: list[int], low: int , high: int):
        if low>=high:
            return
        pivot = low
        pivot_val = a[low]
        i = low + 1
        j = high
        while True:
            while i<=high and a[i]<=pivot_val:
                i+=1
            while j>=low and a[j]>=pivot_val:
                j-=1
            if i==high+1:
                j=high
            if j==low-1:
                j=low
            if i<j:
                #print(f'i = {i}-{a[i]}, j = {j}-{a[j]} swapped')
                a[i], a[j] = a[j], a[i]
                #print(a)
            else:
                break
        if pivot!=j:
            #print(f'i = {i}-{a[i] if i<=high else None}, j = {j}-{a[j]}, pivot = {pivot}-{a[pivot]} swapped')
            a[j],a[pivot] = a[pivot],a[j]
            pivot = j
            #print()
            #print(a)
        #return a[low:j-1], a[j+1:high]
        sort.partition(a,low,pivot-1)
        sort.partition(a,pivot+1,high)

    def quickSort(a: list[int]) -> list[int]:
        l = len(a)
        sort.partition(a,0,l-1)
        return a

    def merge(a: list[int], low: int, mid: int, high: int):
        i = low
        j = mid + 1
        k = 0
        b = [0]*(high-low+1)
        while i<=mid and j<=high:
            if a[i] < a[j]:
                b[k] = a[i]
                k+=1
                i+=1
            else:
                b[k] = a[j]
                k+=1
                j+=1
        while i<=mid:
            b[k] = a[i]
            i+=1
            k+=1
        while j<=high:
            b[k] = a[j]
            j+=1
            k+=1
        #print(b)
        a[low:high+1] = b[0:]

    def split(a: list[int], low: int, high: int):
        if low<high:
            mid = (low + high)//2
            sort.split(a, low, mid)
            sort.split(a, mid+1,high)
            sort.merge(a,low,mid,high)

    def mergeSort(a: list[int]) -> list[int]:
        sort.split(a, 0, len(a)-1)
        return a

ar = []

for i in range(1000):
    ar.append(random.randint(1,999))

time_taken(sort.bubbleSort, ar[:])
time_taken(sort.insertionSort, ar[:])
time_taken(sort.selectionSort, ar[:])
time_taken(sort.quickSort, ar[:])
time_taken(sort.mergeSort, ar[:])
