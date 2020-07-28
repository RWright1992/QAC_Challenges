def hamsterjams(x):
    l_str = x.lower()
    #putting through string as lower case to ignor capitalisation
    count = 0
    if l_str[0:3] == 'am ':
        count +=1
    #checking if start of string begins with am followed by a space
    if l_str[-1:-4:-1] == "ma ":
        count +=1
    #checking if end of string ends with <whitespace>am 
    for i in range(len(l_str)):
        if l_str[i:i+4] == ' am ':
            count += 1
    #iterating through string to check for am inbewtween two words
    
        
    return count


