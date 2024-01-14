list = [
    [0,"sneha","sd@gmail.com",1254541,2000]
]

""" index:
0:account number
1:Name
2:email
3:mobile number
4:bank balance """


account_number = 1

def creat_account():
    global account_number
    name = input("enter name: ")
    mail = input("enter email: ")
    number = input("enter mobile number: ")
    balance = input("enter balance: ")
    list.append([account_number, name, mail, number, balance])
    account_number = account_number + 1

def display():
    print("----------------------account detail----------------------------")
    for e in list:
        print(str(e[0]) + " | " + e[1] + " | " + e[2] + " | " + str(e[3]) + " | " +str(e[4]))
    print("-------------------------------------------------------------------")

while True:
    print("1.create new account")
    print("2.display list")
    print("0.exit")

    inpute_number = input("choose number: ")

    match inpute_number:
        case '1':
            creat_account()
        case '2':
            display()
        case '0':
            break
        case other:
            print("wrong inpute")