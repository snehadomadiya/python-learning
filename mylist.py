""" mylist = [10, 22, 35, 48, 50, 41, 20, 56, 85, 15, 52]
mylist.append(56)

print(mylist)

mylist.remove(50)

print(mylist) """

""" def is_value_present(mylist, value):
    return value in mylist

mylist = [11,12,15,8,15,19,20]

value_check = 19
if is_value_present(mylist, value_check):
    print("{value_check} is present in the list.")
else:
    print("{value_check} is not present in the list.") """

""" def is_value_present(mylist, value):
    return value in mylist

mylist = [11,12,15,8,15,19,20,25,75,62,15,75]

value_check = 99
if is_value_present(mylist, value_check):
    print("{value_check} is present in the list.")
else:
    print("{value_check} is not present in the list.") """

odd = []
even = []

for num in range(1, 21):
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Odd Numbers:", odd)
print("Even Numbers:", even)