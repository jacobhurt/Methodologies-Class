"""
 * SortHelper.java
 *
 * Computer Science E-22
 *
 * YOU SHOULD *NOT* NEED TO MODIFY THIS FILE.
"""
   
class SortHelper():
    """
     * swap - swap the values of the elements in positions a and b
     * in both the keys and dataItems arrays.
    """
    def swap(keys, data, a, b):
        keys[a], keys[b] = keys[b], keys[a]
        data[a], data[b] = data[b], data[a] 
    
    """
     * partition - helper method for qSort. 
     * Partitions the array/subarray keys[first:last] and also
     * makes the corresponding swaps to the values in the 
     * data array.
    """
    def partition(keys, data, first, last):
        pivot = keys[first]
        i = first + 1    # set index going left to right
        j = last         # set index going right to left
        while True:
            while i <= j and keys[i] <= pivot: # find a number >= pivot
                i = i + 1
            while i <= j and keys[j] >= pivot: # find a number <= pivot
                j = j - 1
            if i < j:                           
                SortHelper.swap(keys, data, i, j)     # put numbers on the correct side
                i = i + 1                       # keep going
                j = j - 1                       # keep going
            else:
                SortHelper.swap(keys, data, first, j)      # place pivot in place
                return j                        # index of pivot
       
    """
     * qSort - recursive method that does the work for quickSort.
     * Sorts the array/subarray keys[first:last], while also
     * making the corresponding changes to the values in the 
     * data array.
    """
    def qSort(keys, data, first, last):
        split = SortHelper.partition(keys, data, first, last)
        if first < split:
            SortHelper.qSort(keys, data, first, split - 1)         # left sublist [0:pivot)
        if last > split + 1:
            SortHelper.qSort(keys, data, split + 1, last)          # right sublist(pivot:last]
    
    """
     * quicksort. Sorts the keys array, while also
     * making the corresponding changes to the values in the 
     * dataItems array. For example, if a key is moved from 
     * position i to position j in the keys array, then the
     * corresponding data item is also moved from position i
     * to position j in the dataItems array.
    """ 
    def quickSort(keys, data):
        SortHelper.qSort(keys, data, 0, len(keys)-1)
