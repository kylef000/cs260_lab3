import sys
import time

'''
Quicksort:
Best Case: O(n log n)
Average case: O(n log n)
Worst case: O(n^2)

Insertion sort:
Worst case: O(n^2) compares, swaps
Average case: O(n^2) compares, swaps
Best Case: O(n) compares, O(1) swaps
'''

from InsertionSort import IS

def quickSort(lyst, K):
    def recurse(left, right):
            if left < right:
                pivotPosition = partition(lyst, left, right)
                if abs(left - right) > K:
                    recurse(left, pivotPosition - 1);
                    recurse(pivotPosition + 1, right)
                else:
                    IS(lyst, len(lyst) - pivotPosition)
                    
    def partition(lyst, left, right):
        # Find the pivot and exchange it with the last item
        middle = (left + right) // 2
        pivot = lyst[middle]
        lyst[middle] = lyst[right]
        lyst[right] = pivot
        # Set boundary point to first position
        boundary = left
        # Move items less than pivot to the left
        for index in range(left, right):
            if lyst[index] < pivot:
                lyst[index],lyst[boundary] = lyst[boundary],lyst[index]
                boundary += 1
        # Exchange the pivot item and the boundary item
        lyst[right],lyst[boundary] = lyst[boundary],lyst[right]
        return boundary   

    recurse(0, len(lyst)-1)
    
def main():

    filename = "file1"
    length = int(input("How many lines? "))
    K = int(input("K value? "))
    a = []
    file = open(filename,"r")
    for i in range(0,length,1):
        a.append(int(file.readline()))

    t1 = time.process_time()
    quickSort(a, K)
    t2 = time.process_time()

    print(t2-t1)
#    print(a)


if __name__ == "__main__":
    main()
            
                
