# Corey Sokol

# Defines a insertion sort function
def insertionSort(alist):
    
    # For loop that creates the passes and sets the originalNum variable to the
    # current value of i in the loop. currentPos is assigned as the current position in the loop
    for i in range(1, len(alist)):
        originalNum = alist[i]
        currentPos = i

        # Checks if the current position is greater than 0 and that the previous item in the list
        # is greater than the originalNum stored
        while currentPos>0 and alist[currentPos-1]>originalNum:
            
            # The previous value is set as the current value
            alist[currentPos]=alist[currentPos-1]
            currentPos = currentPos-1
        
        # Set the currentPos in alist to the originalNum variable we stored initially.
        # Moves the item towards the beginning of the list the smaller they are.
        alist[currentPos] = originalNum
        
        

alist = [2, 10, 1, 3, 9, 6, 4, 5, 8, 7]
insertionSort(alist)
print(alist)