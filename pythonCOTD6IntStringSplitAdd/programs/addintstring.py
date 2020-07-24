def factnumber(input):
    string_i = str(input)
    string_ii = str(input) + str(input)
    string_iii = str(input) + str(input) + str(input)
    string_iiii = str(input) + str(input) + str(input) + str(input)
#turning my input into 4 strings and concatinating so i can get a, aa, aaa and aaaa
    addition = int(string_i) + int(string_ii) + int(string_iii) + int(string_iiii)
#adding my 4 strings together as integers
    return addition

'''
Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)
'''

