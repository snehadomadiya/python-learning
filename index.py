""" mylist = ["smit","sneha","akta"]

print(mylist)
index = mylist.index("sneha")
print("index of sneha:" + str(index))
mylist[index] = "akash"

print(mylist) """

mylist = ["smit","sneha","akta"]

print(mylist)
index = mylist.index("sneha")
print("index of sneha:" + str(index))
mylist.insert(index,"akash")

print(mylist)