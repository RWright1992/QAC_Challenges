def sortstring(input1):
    #splitstring = input1.split()
    #assigning my varaible splitstring to a string to be split by a space to indicate the start and end of each word
    alphasort = dict.fromkeys(input1.split())
    #sort my list
    #removedup = set(alphasort)
    join1 = ' '.join(sorted(alphasort))    
    #assigning my varaible remove to the function set to remove duplicates
    return str(join1)
    #bringing my list together as a string
    
   

#sortstring('hello world and practice makes perfect and hello world again') 

