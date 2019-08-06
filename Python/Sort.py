"""
 * Sort.py
 *
 * Adopted from: omputer Science E-22, Harvard University
 *
 * Your solution to programming problem 1 should go in this file.
 *
 * IMPORTANT: Your solution to programming problem 3 should go in 
 * SortCount.py, rather than in this file.
 *
 * To call one of these methods from another class, precede its name
 * by the name of the class.  For example:
 *
 *     Sort.bubbleSort(arr)
 */

/**
 * Sort - a class containing implementations of various array-sorting
 * algorithms. Each sorting method takes an array of ints, and 
 * assumes that the array is full. The methods sort the array in place,
 * altering the original array.
"""
from random import *

class Sort():
    
    # swap - swap the values of two variables.
    # Used by several of the sorting algorithms below.
    def swap(alist, i, j):
        alist[i], alist[j] = alist[j], alist[i]
        
    # selectionSort
    def selectionSort(alist):
        for i in range(len(alist)):
            indexMin = i
            # find the smallest index
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[indexMin]:
                    indexMin = j
            Sort.swap(alist, i, indexMin)

    # insertionSort 
    def insertionSort(alist):
        for i in range(1, len(alist)):
            # save a copy of the element and index to be inserted.
            val = alist[i]    
            pos = i
            # save a copy of the element to be inserted.
            while pos >= 1 and alist[pos-1] > val:     
                alist[pos] = alist[pos-1]
                pos = pos - 1
            # Put the element in place.
            alist[pos] = val  

    # shellSort
    def shellSort(alist):
        gap = len(alist) // 2  # calculate the gap
        # Do insertion sort for each gap. 
        while gap >= 1:
            for start in range(gap):
                # modified insertion sort
                for i in range(start + gap, len(alist), gap):
                    # save a copy of the element and index to be inserted.
                    val = alist[i]
                    pos = i
                    # save a copy of the element to be inserted.
                    while pos >= gap and alist[pos-gap] > val:
                        alist[pos] = alist[pos-gap]
                        pos = pos - gap
                    # Put the element in place.
                    alist[pos] = val  
            # Calculate gap for next pass.
            gap = gap // 2

    # bubbleSort
    def bubbleSort(alist):
        for i in range(len(alist)):
            for j in range(len(alist)-1):
                if alist[j] > alist[j+1]:
                    Sort.swap(alist, j, j+1)

    # partition - helper method for qSort 
    def partition(alist, first, last):
        pivot = alist[first]
        i = first + 1    # set index going left to right
        j = last         # set index going right to left

        while True:
            while i <= j and alist[i] <= pivot: # find a number >= pivot
                i = i + 1
            while i <= j and alist[j] >= pivot: # find a number <= pivot
                j = j - 1
            if i < j:                           
                Sort.swap(alist, i, j)          # put numbers on the correct side
                i = i + 1                       # keep going
                j = j - 1                       # keep going
            else:
                Sort.swap(alist, first, j)      # place pivot in place
                return j                        # index of pivot

    # qSort - recursive method that does the work for quickSort */
    def qSort(alist, first, last):
        split = Sort.partition(alist, first, last)
        if first < split:
            Sort.qSort(alist, first, split - 1)         # left sublist [0:pivot)
        if last > split + 1:
            Sort.qSort(alist, split + 1, last)          # right sublist(pivot:last]

    # quicksort 
    def quickSort(alist):
        Sort.qSort(alist, 0, len(alist)-1)
        
    # merge - helper method for mergesort 
    def merge(alist, temp, leftStart, leftEnd, rightStart, rightEnd): 
        i = leftStart
        j = rightStart
        k = leftStart
        # merge the two lists as long as both lists have elements
        while i <= leftEnd and j <= rightEnd:
            if alist[i] < alist[j]:
                temp.insert(k, alist[i])
                i = i + 1
            else:
                temp.insert(k, alist[j])
                j = j + 1
            k = k + 1
        # run out remaining elements in left list     
        while i <= leftEnd:
            temp.insert(k, alist[i])
            i = i + 1
            k = k + 1
        # run out remaining elelments in right list
        while j <= rightEnd:
            temp.insert(k, alist[j])
            j = j + 1
            k = k + 1
        # copy temp list back to original    
        for i in range(leftStart, rightEnd + 1):
            alist[i] = temp[i]
        
    # mSort - recursive method for mergesort 
    def mSort(alist, temp, start, end):
        if start >= end:
            return    
        mid = (start + end) // 2                              # split the list in half
        Sort.mSort(alist, temp, start, mid)                   # sort left half
        Sort.mSort(alist, temp, mid + 1, end)                 # sort the right half                
        Sort.merge(alist, temp, start, mid, mid + 1, end)     # merge the two halfs
    
    # mergesort 
    def mergeSort(alist):
        temp = []
        Sort.mSort(alist, temp, 0, len(alist) - 1)
    
    # printList - prints the specified array in the following form:
    # { alist[0] alist[1] ... }
    def printList(alist):
        print("{ ", end="")
        for i in range(len(alist)):
            print(str(alist[i]) + " ", end="")
        print("}")
        
    # coptList - copies one list to another
    def copyList(source, dest):
        for i in range(len(source)):
            dest[i] = source[i]

    def removeDups(alist):
        length = len(alist)
        index = 0
        count = 0
        while not index==len(alist)-1:
            if alist[index]==alist[index+1]:
                alist.pop(index+1)
                count=count+1
            else:
                index=index+1
        addCount = 0
        while not count==addCount:
            alist.append(0)
            addCount=addCount+1
        return length-count
        
def main():
    NUM_ELEMENTS = 10
    NUM_VARS = 5
    orig = []
    copy = []
    for i in range(NUM_ELEMENTS):
        temp = randint(0, NUM_ELEMENTS * NUM_VARS)
        orig.append(temp)
        copy.append(temp)

    # original list 
    print("original list:\t", end="")
    Sort.printList(orig)

    # selection sort
    Sort.copyList(orig, copy)
    Sort.selectionSort(copy)
    print("selection sort:\t", end="")
    Sort.printList(copy)

    # insertion sort
    Sort.copyList(orig, copy)
    Sort.insertionSort(copy)
    print("insertion sort:\t", end="")
    Sort.printList(copy)

    # Shell sort
    Sort.copyList(orig, copy)
    Sort.shellSort(copy)
    print("Shell sort:\t", end="")
    Sort.printList(copy)

    # bubble sort
    Sort.copyList(orig, copy)
    Sort.bubbleSort(copy)
    print("bubble sort:\t", end="")
    Sort.printList(copy)

    # quick sort
    Sort.copyList(orig, copy)
    Sort.quickSort(copy)
    print("quick sort:\t", end="")
    Sort.printList(copy)

    # add remove dulpicates here
    #Sort.copyList(orig, copy)
    distinct = Sort.removeDups(copy)
    print("removed duplicates")
    print("distinct elements:\t" + str(distinct))
    Sort.printList(copy)

main()
