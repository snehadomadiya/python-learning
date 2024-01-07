list = [1,2,3,4,5,6,7,8,9]

""" i = 0
while list[i] < 6:
    print(list[i])
    i = i + 1 """

""" i = 0
while list[i] < 6:
    print(list[i])
    if i == 2:
        break
    i = i + 1 """


i = 0
while list[i] < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)
    

