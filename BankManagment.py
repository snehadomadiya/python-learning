list = [
    [0,"sneha","sd@gmail.com",123456789,20000,156],
    [1,"chirag","cd@gmail.com",987456321,40000,143]
]

""" index:
0:account number
1:Name
2:email
3:mobile number
4:bank balance
5:password """


account_number = 1

def creat_account():
    global account_number
    name = input("enter name: ")
    mail = input("enter email: ")
    number = input("enter mobile number: ")
    balance = input("enter balance: ")
    password = input("enter password: ")
    list.append([account_number, name, mail, number, balance, password])
    account_number = account_number + 1

def display():
    print("----------------------account detail----------------------------")
    for e in list:
        print(str(e[0]) + " | " + e[1] + " | " + e[2] + " | " + str(e[3]) + " | " +str(e[4]) + " | " + str(e[5]))
    print("-------------------------------------------------------------------")

def balance_check():
    account = input("enter details: ")
    for e in list:
        if str(e[0]) == account or account == e[1]:
            print("----------------------account detail----------------------------")
            print("balance: " + str(e[4]))
            print("-------------------------------------------------------------------")
    return print("-----xxx--------Account do not exist---------------xxx-------------")

def password():
    enter_password = input("enter password: ")
    enter_name = input("enter your name: ")
    for e in list:
        if str(e[5]) == enter_password and e[1] == enter_name:
            print("----------------------account detail----------------------------")
            print(str(e[0]) + " | " + e[1] + " | " + e[2])
            print("-------------------------------------------------------------------")

while True:
    print("1.create new account")
    print("2.display list")
    print("3.check balance")
    print("4.password")
    print("0.exit")

    inpute_number = input("choose number: ")

    match inpute_number:
        case '1':
            creat_account()
        case '2':
            display()
        case '3':
            balance_check()
        case '4':
            password()
        case '0':
            break
        case other:
            print("wrong inpute")