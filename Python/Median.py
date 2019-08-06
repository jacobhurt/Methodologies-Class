"""
 * Median.py
 *
 * Adopted from by Computer Science E-22, Harvard University
 * 
 * Modifed by:      jacob hurt 
 * Date modified:   3/7/16
"""

from Sort import *

class Median():
    # partition - helper method for your recursive median-finding method */
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

     # findMedian - "wrapper" method for your recursive median-finding method.
     # It just makes the initial call to that method, passing it
     # whatever initial parameters make sense.
     
    def findMedian(alist):
        Median.median(alist,0,len(alist)-1)
        if len(alist) % 2 ==0:
            print ("Median Value(for even): ", ((alist[len(alist)//2])+(alist[len(alist)//2 - 1]))/2)
        else:
            print ("Median Value(for odd): ", alist[len(alist)//2])

    # add an appropriate call to your recursive method
    def median(alist,first,last):
        med = Median.partition(alist,first,last)
        if (first<med and med>len(alist)//2-1):
            Median.median(alist,first,med)
        if (last>med+1 and med<= len(alist)//2-1):
            Median.median(alist,med+1,last)
    
    
    # Put the definition of your recursive median-finding method below. 
    
    def main():
        # the median of this array is 15
        oddLength = [4, 18, 12, 34, 7, 42, 15, 22, 5]
        
        # the median of this array is the average of 15 and 18 = 16.5
        evenLength = [4, 18, 12, 34, 7, 42, 15, 22, 5, 27]
        
        
        # Put code to test your method here.
        print("Odd Length's list: " , oddLength)
        print("Even Length's list: " , evenLength)
        Median.findMedian(oddLength)
        Median.findMedian(evenLength)
Median.main()
        

