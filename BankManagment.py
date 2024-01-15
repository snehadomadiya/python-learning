list = [
    [0,"sneha","sd@gmail.com",123456789,10000,"123"],
    [1,"chirag","cd@gmail.com",987456321,10000,"143"]
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
        if str(e[0]) == account or account == e[1] or e[2] == account:
            print("----------------------account detail----------------------------")
            print("balance: " + str(e[4]))
            print("-------------------------------------------------------------------")
        elif (list[len(list)-1][0] != account or list[len(list)-1][1] != account or list[len(list)-1][2] != account) and (list[len(list)-1][0] == e[0] or list[len(list)-1][1] == e[1] or list[len(list)-1][2] == e[2]):
            print("-----xxx--------Account do not exist---------------xxx-------------")

def withdraw():
    enter_account= input("enter your account number: ")
    enter_password = input("enter password: ")
    for e in list:
        if e[5] == enter_password and e[0] == int(enter_account):
            withdraw_ammount = input("enter your amount: ")
            e[4] = e[4] - int(withdraw_ammount)
        elif list[len(list)-1][0] != enter_account and list[len(list)-1][0] == e[0]:
            print("-----xxx--------Account do not exist---------------xxx-------------")

def add_money():
    account = input("enter detail: ")
    amount = input("add money: ")

    for e in list:
        if str(e[0] )== account or e[1] == account or e[2] == account:
            e[4] = e[4] + int(amount)
        elif (list[len(list)-1][0] != account or list[len(list)-1][1] != account or list[len(list)-1][2] != account) and (list[len(list)-1][0] == e[0] or list[len(list)-1][1] == e[1] or list[len(list)-1][2] == e[2]):
            print("-----xxx--------Account do not exist---------------xxx-------------")


while True:
    print("1.create new account")
    print("2.display list")
    print("3.check balance")
    print("4.withdraw")
    print("5.add money")
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
            withdraw()
        case '5':
            add_money()
        case '0':
            break
        case other:
            print("wrong inpute")