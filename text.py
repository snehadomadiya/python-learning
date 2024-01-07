""" list = []
while True:
    x = input("Enter value: ")
    list.append(x)
    if x == "0":
        break
    print(list) """

name_list = ["smit"]


while True:
    print("--------------------------------------------------------")
    print("1.Add Name")
    print("2.Disply Name")
    print("3.Remove Name")
    print("4.exit")

    input_name = input("Choise a number: ")

    if input_name == "2":
        print(name_list)

    elif input_name == "1":
        name = input("Enter name: ")
        if name in name_list:
            print(name + " name is already in list.")
        else:
            name_list.append(name)

    elif input_name == "3":
        name = input("remove name: ")
        if name in name_list:
            name_list.remove(name)
        else:
            print("This name is not in list")

    elif input_name == "4":
        break

    else:
        print("wrong input")
        

        

