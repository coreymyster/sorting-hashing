# Corey Sokol

# Defines the function to bubble sort
def bubbleSort(alist):
    # For loop that creates the passes.
    # After the below loop concludes each time, we create another pass and run through
    # the below loop again.
    for listPass in range(len(alist)-1, 0, -1):
        
        # Passes through the entire list once. When done loop breaks and the above for loop
        # creates another pass where we continue below.
        
            # i is used as the index of the list based on listPass' range
            for i in range(listPass):
                # If the item on the left is greater than the item to the right on the list
                # then we swap them
                if alist[i] > alist[i + 1]:
                    temp = alist[i]
                    alist[i] = alist[i + 1]
                    alist[i + 1] = temp


alist = [2, 10, 1, 3, 9, 6, 4, 5, 8, 7]
bubbleSort(alist)
print(alist)