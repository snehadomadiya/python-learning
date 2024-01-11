""" nested_list = [
    ["smit", 23,"Berlin","data"],
    ["sneha", 28,"Berlin","engineer"],
    ["Maitri", 18,"Erlangan","MBA"],
    ["akash", 25,"India","data"],
    ["Akta", 29,"India","softwere developer"],
]
 """

""" 
for i in nested_list:
    if i[1]>24:
        print( i[0] + " from " + i[2] + " and age of " + str(i[1]) )

#Smit from India and age of 28 """

""" for e in nested_list:
    if e[0] == "smit":
        print(e[0] + " from " + e[2]) """

""" for e in nested_list:
    print(e[0])
    print(e[1])
    print(e[2]) """

""" for e in nested_list:
    if e[3] == "data":
        print(e[0] + " is studing " + e[3]) """

nested_list = [
    ["smit", 23,"surat"],
    ["sneha", 28,"vadodara"],
    ["Maitri", 18,"ahemdabad"],
    ["akash", 25,"surat"],
    ["Akta", 16,"banglore"],
    ["venus", 15,"jamnagar"],
    ["simran", 16,"mumbai"],
    ["ridhi", 17,"delhi"]
]

for e in nested_list:
    if e[1] > 18:
        print(e[0] + " is giving vote.")
    else:
        print(e[0] + " is not giving vote.")