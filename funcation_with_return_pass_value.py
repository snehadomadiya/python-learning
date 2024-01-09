""" list = []
while True:
    x = input("Enter value: ")
    list.append(x)4
    
    if x == "0":
        break
    print(list) """

name_list = ["smit"]

def disply():
    print(name_list)

def add_name():
        name = ip_fun("Enter any name: ")
        if name in name_list:
            print(name + " name is already in list.")
        else:
            name_list.append(name)

def remove_name():
    name = ip_fun("Enter remove name: ")
    if name in name_list:
        name_list.remove(name)
    else:
        print("This name is not in list")

def find_name():
    name = ip_fun("Enter any name: ")
    if name in name_list:
        print(name + " is availabale in list")
    else:
        print(name + " is not available in list")
        
def ip_fun(msg):
    inpute_var = input(msg)
    return inpute_var




while True:
    print("--------------------------------------------------------")
    print("1.Add Name")
    print("2.Disply Name")
    print("3.Remove Name")
    print("4.exit")
    print("5.find name")

    input_name = input("Choise a number: ")

    if input_name == "2":
        disply()

    elif input_name == "1":
        add_name()

    elif input_name == "3":
       remove_name()
    elif input_name == "4":
        break
    elif input_name == "5":
        find_name()

    else:
        print("wrong input")
        


