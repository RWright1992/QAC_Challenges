def seven_notfive(int1, int2):
    i1 = int(int1)
    i2 = int(int2)
    emptlist = []
    for i in range(i1, i2):
        if (i%7 == 0) and (i%5 != 0):
            emptlist.append(str(i))
    return (','.join(emptlist))


print(seven_notfive(2000, 3200))