# find a number in list using forloop
""" list = [25,12,65,89,65]
#num var for find a number
num = 65

for x in list:
    if num==x:
        print(str(num) + " in list "+ str(count)+ " time")
 """

# Count a number in list 
""" list = [25,12,65,89,65]
findNUm = 65
count=0

for x in list:
    if x==findNUm:
        count=count+1
print(str(findNUm) + " in list "+ str(count)+ " time") """


# count two number in list
""" list = [11,17,12,18,46,12,89,12,18,25]

findnum1= 18
findnum2 = 12
count1=0
count2=0

for x in list:
    if x==findnum1:
        count1=count1 + 1
    if x==findnum2:
        count2=count2 + 1

print(str(findnum1) + " in list " + str(count1) + " time")
print(str(findnum2) + " in list " + str(count2) + " time") """

names = ["smit", "esha", "sneha", "alas", "akta", "avish"]
ages = [26, 18, 28, 21, 12, 22]

for e in range(len(names)):
    if ages[e] > 25:
        print(names[e])