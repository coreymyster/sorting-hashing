# Corey Sokol

# Creates the hash function to create hash values for strings in a list
def hashFunction(alist):
    
    # For loop to get first string in a list and sets the hash name (hName) variable to 0
    for name in alist:
        hName = 0
        
        # For loop to get each character of the string we are looping through
        for char in name:
            # Converts each character to an ordinal value and increments hName
            hName = hName + ord(char)
        # Creates the hashvalue by taking hNames total and dividng by the list size.
        # The remainder becomes the location in the hash table.
        hNum = hName % len(alist)
        
        # For testing purposes this print the hash value for each item
        print(hNum)
        
        # Replace current value at the hNum index with the name in the list
        hash[hNum] = name
        


# A test list of names
alist = ['Penny', 'Avery', 'Jack', 'Batman', 'Superman', 'Barbosa', 'Luke']

# Creates the hash table
hash = [None] * 7

#Original hash table
print(hash)

hashFunction(alist)

# Hash table once values are added. No collisions are present creating a perfect hash.
print(hash)