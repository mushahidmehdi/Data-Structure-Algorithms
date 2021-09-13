# insertionSort(array)
#  mark first element as sorted
#  for each unsorted element X
#    'extract' the element X
 #   for j <- lastSortedIndex down to 0
 #     if current element j > X
 #       move sorted element to the right by 1
 #   break loop and insert X here
#end insertionSort
# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)