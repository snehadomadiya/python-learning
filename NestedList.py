nested_list = [
    ["smit", 23,"Berlin"],
    ["sneha", 28,"Berlin"],
    ["Maitri", 18,"Erlangan"],
    ["akash", 25,"India"],
    ["Akta", 29,"India"],
]
""" 
for i in nested_list:
    if i[1]>24:
        print( i[0] + " from " + i[2] + " and age of " + str(i[1]) )

#Smit from India and age of 28 """


for e in nested_list:
    print(e[0])
    print(e[1])
    print(e[2])