def sortstring(input1):
    splitstring = input1.split()
    #assigning my varaible splitstring to a string to be split by a space to indicate the start and end of each word
    alphasort = splitstring.sort()
    #sort my list
    removedup = set(alphasort)
    #assigning my varaible remove to the function set to remove duplicates
    return ' '.join(removedup)    
    #bringing my list together as a string
    
   

#sortstring('hello world and practice makes perfect and hello world again') 

