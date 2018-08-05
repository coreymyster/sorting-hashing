# Corey Sokol

# Defines a selection sort function
def selectionSort(alist):
    # For loop that creates the passes and sets the maxNum variable to the 0 index.
    # After the below loop concludes each time, we create another pass and run through
    # the below loop again.
    for listPass in range(len(alist) - 1, 0, -1):
        maxNum = 0
        
        # Passes through the entire list once. When done loop breaks and the above for loop
        # creates another pass where we continue below.
        # i is used as the index of the list based on listPass' range
        for i in range(1, listPass + 1):
            # If the current item at index i is greater, then maxNum is updated with that index
            if alist[i] > alist[maxNum]:
                maxNum = i
        
        # Checks the index of the pass in the loop and changes out the last index for the highest number
        # The last index then swaps places with where the highest number used to be in the list.
        temp = alist[listPass]
        alist[listPass] = alist[maxNum]
        alist[maxNum] = temp
            

alist = [2, 10, 1, 3, 9, 6, 4, 5, 8, 7]
selectionSort(alist)
print(alist)