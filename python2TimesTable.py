#Times Table grid

'''
n= int(input('Please enter your number'))
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))

for i in m:
    i = [str(j).rjust(len(str(m[-1][-1]))+1) for j in i]
    print(''.join(i))
'''

def timetable(n):
    line =""
    for row in range(1,n+1):
        for column in range(1, n+1):
            line = line +str(row*column) + "\t"
        line = line +"\n"
    return line

number = int(input("Enter your number"))
print(timetable(number))
