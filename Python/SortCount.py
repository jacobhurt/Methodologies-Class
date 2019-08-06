"""
 * SortCount.py
 *
 * Adopted from: Computer Science E-22, Harvard University
 *
 * Modified by:   <your name>, <your e-mail address>
 * Date modified: <current date>
"""

"""
 * This class contains implementations of various array-sorting
 * algorithms.  All comparisons and moves are performed using helper
 * methods that maintain counts of these operations.  Each sort method
 * takes an array of integers.  The methods assume that all of the
 * elements of the array should be sorted.  The algorithms sort the array
 * in place, altering the original list.
"""

from random import *
import math

class SortCount():

    MAX_VAL = 65536 # the integers in the test arrays are in the range 0, ..., MAX_VAL 
    compares = 0    # total number of comparisons
    moves = 0       # total number of moves

    # compare - a wrapper that allows us to count comparisons.
    def compare(comparison):
        SortCount.compares += 1
        return comparison

    # swap - swap the values of two variables.
    # Used by several of the sorting algorithms below.
    def swap(alist, a, b):
        alist[a], alist[b] = alist[b], alist[a]
        SortCount.moves += 3

    # randomList- creates an list of randomly generated integers
    # with the specified number of elements and the specified
    # maximum value
    def randomList(n, maxVal = MAX_VAL):
        alist = n * [0]
        for i in range(len(alist)):
            alist[i] = randrange(0, maxVal)
        return alist

    # Sets the counts of moves and comparisons to 0.
    def initStats():
        SortCount.compares = 0
        SortCount.moves = 0

    # Prints the current counts of moves and comparisons.
    def printStats():
        if SortCount.compares == 0:
            spaces = 0
        else:
            spaces = int(math.log(SortCount.compares, 10))
        for i in range(10 - spaces):
            print(" ", end="")
        print(str(SortCount.compares) + " comparisons\t");

        if SortCount.moves == 0:
            spaces = 0
        else:
            spaces = int(math.log(SortCount.moves, 10))
        for i in range(10 - spaces):
            print(" ", end="")
        print(str(SortCount.moves) + " moves")

    # selectionSort
    def selectionSort(alist):
        for i in range(len(alist)):
            indexMin = i
            # find the smallest index
            for j in range(i + 1, len(alist)):
                if SortCount.compare(alist[j] < alist[indexMin]):
                    indexMin = j
            SortCount.swap(alist, i, indexMin)

    # insertionSort 
    def insertionSort(alist):
        for i in range(1, len(alist)):
            # save a copy of the element and index to be inserted.
            val = alist[i]    
            pos = i
            SortCount.moves += 1
            # save a copy of the element to be inserted.
            while pos >= 1 and SortCount.compare(alist[pos-1] > val):     
                alist[pos] = alist[pos-1]
                pos = pos - 1
                SortCount.moves += 1
            # Put the element in place.
            alist[pos] = val
            SortCount.moves += 1

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
                    SortCount.moves += 1
                    while pos >= gap and SortCount.compare(alist[pos-gap] > val):
                        alist[pos] = alist[pos-gap]
                        pos = pos - gap
                        SortCount.moves += 1
                    # Put the element in place.
                    alist[pos] = val
                    SortCount.moves += 1
            # Calculate gap for next pass.
            gap = gap // 2

    # bubbleSort
    def bubbleSort(alist):
        for i in range(len(alist)):
            for j in range(len(alist)-1):
                if SortCount.compare(alist[j] > alist[j+1]):
                    SortCount.swap(alist, j, j+1)

    # partition - helper method for qSort 
    def partition(alist, first, last):
        pivot = alist[first]
        SortCount.moves += 1
        i = first + 1    # set index going left to right
        j = last         # set index going right to left

        while True:
            while i <= j and SortCount.compare(alist[i] <= pivot):      # find a number >= pivot
                i = i + 1
            while i <= j and SortCount.compare(alist[j] >= pivot):      # find a number <= pivot
                j = j - 1
            if i < j:                           
                SortCount.swap(alist, i, j)          # put numbers on the correct side
                i = i + 1                            # keep going
                j = j - 1                            # keep going
            else:
                SortCount.swap(alist, first, j)      # place pivot in place
                return j                             # index of pivot

    # qSort - recursive method that does the work for quickSort */
    def qSort(alist, first, last):
        split = SortCount.partition(alist, first, last)
        if first < split:
            SortCount.qSort(alist, first, split - 1)         # left sublist [0:pivot)
        if last > split + 1:
            SortCount.qSort(alist, split + 1, last)          # right sublist(pivot:last]

    # quicksort 
    def quickSort(alist):
        SortCount.qSort(alist, 0, len(alist)-1)
        
    # merge - helper method for mergesort 
    def merge(alist, temp, leftStart, leftEnd, rightStart, rightEnd): 
        i = leftStart
        j = rightStart
        k = leftStart
        
        while i <= leftEnd and j <= rightEnd:
            if SortCount.compare(alist[i] < alist[j]):
                temp.insert(k, alist[i])
                i = i + 1
            else:
                temp.insert(k, alist[j])
                j = j + 1
            k = k + 1
            SortCount.moves += 1
            
        while i <= leftEnd:
            temp.insert(k, alist[i])
            i = i + 1
            k = k + 1
            SortCount.moves += 1
        
        while j <= rightEnd:
            temp.insert(k, alist[j])
            j = j + 1
            k = k + 1
            SortCount.moves += 1
            
        for i in range(leftStart, rightEnd + 1):
            alist[i] = temp[i]
            SortCount.moves += 1
        
    # mSort - recursive method for mergesort 
    def mSort(alist, temp, start, end):
        if start >= end:
            return    
        mid = (start + end) // 2                                   # split the list in half
        SortCount.mSort(alist, temp, start, mid)                   # sort left half
        SortCount.mSort(alist, temp, mid + 1, end)                 # sort the right half                
        SortCount.merge(alist, temp, start, mid, mid + 1, end)     # merge the two halfs
    
    # mergesort 
    def mergeSort(alist):
        temp = []
        SortCount.mSort(alist, temp, 0, len(alist) - 1)

        #swapSort
    def swapsort(alist):
        for i in range(len(alist)):
            for j in range(len(alist)-1):
                if SortCount.compare(alist[j]>alist[i]):
                    SortCount.swap(alist,j,i)
    
    # almostSortedArray - creates an almost sorted array of integers
    # with the specified number of elements
    def almostSortedList(n):
        # Produce a random array and sort it. 
        alist = SortCount.randomList(n)
        SortCount.quickSort(alist)
          
        # Move one quarter of the elements out of place by between 1
        # and 5 places
        for i in range(n // 8):
            j = int(random() * n)
            displace = -5 + int(random() * 11)
            k = j + displace
            if k < 0:
                k = 0
            if k > n - 1:
                k = n - 1
            SortCount.swap(alist, j, k)
        return alist

    # Copys the src list to the dest list
    def listCopy(source, dest):
        for i in range(len(source)):
            dest[i] = source[i]
        
    # Prints the specified list in the following form:
    # { lista[0] lista[1] ... }
    def printList(alist):
        # Don't print it if it's more than 10 elements.
        if len(alist) > 10:
            return
        print("{ ", end="")
        for i in range(len(alist)):
            print(str(alist[i]) + " ", end="")
        print("}")

def main():

    # Get various parameters from the user.
    numItems = eval(input("How many items in the list? "))
    listType = input("Random (r), almost sorted (a), or fully sorted (f)? ")
    print("")

    a = numItems * [0]       # initialize the list
    asave = numItems * [0]   # and a copy of it
        
    # Create the lists.   
    if listType in "Aa":
        a = SortCount.almostSortedList(numItems)
    else:
        a = SortCount.randomList(numItems)
        if listType in "Ff":
            SortCount.quickSort(a)

    SortCount.listCopy(a, asave)
    SortCount.printList(a)

    # Try each of the various algorithms, starting each time 
    # with a fresh copy of the initial array.         
    print("quickSort:\t\t")
    SortCount.listCopy(asave, a)
    SortCount.initStats()
    SortCount.quickSort(a)
    SortCount.printStats()
    SortCount.printList(a)

    print("mergeSort:\t\t")
    SortCount.listCopy(asave, a)
    SortCount.initStats()
    SortCount.mergeSort(a)
    SortCount.printStats()
    SortCount.printList(a)

    print("shellSort:\t\t")
    SortCount.listCopy(asave, a)
    SortCount.initStats()
    SortCount.shellSort(a)
    SortCount.printStats()
    SortCount.printList(a)

    print("insertionSort:\t\t")
    SortCount.listCopy(asave, a)
    SortCount.initStats()
    SortCount.insertionSort(a)
    SortCount.printStats()
    SortCount.printList(a)

    print("selectionSort:\t\t")
    SortCount.listCopy(asave, a)
    SortCount.initStats()
    SortCount.selectionSort(a)
    SortCount.printStats()
    SortCount.printList(a)

    print("bubbleSort:\t\t")
    SortCount.listCopy(asave, a)
    SortCount.initStats()
    SortCount.bubbleSort(a)
    SortCount.printStats()
    SortCount.printList(a)

    print("SwapSort:\t\t")
    SortCount.listCopy(asave, a)
    SortCount.initStats()
    SortCount.swapsort(a)
    SortCount.printStats()
    SortCount.printList(a)

main()
