list = [
    ["Q12354", "Sawarni","sc@gmail.com",3985645458,"data"],
    ["Q12548","aadhya","ad@gmail.com",9852421222,"MBA"],
    ["Q1257","sweta","sr@gmail.com",95632110,"data"],
    ["Q0215","yashvi","ys@gmail.com",6545212,"IT"],

]

""" index:
0:student Q number
1:student Name
2:gmail
3:mobile number
4:course """

q_number = 1234

def add_student_detail():
    global q_number
    name = input("enter name: ")
    email = input("enter email: ")
    mobile_number = input("enter mobile number: ")
    course = input("enter course: ")

    list.append(["Q" + str(q_number),name,email,mobile_number,course])
    q_number = q_number + 1

def disply():
    print("************************student detail***************************")
    for e in list:
        print(e[0] + " | " + e[1] + " | " + str(e[3]) + " | " + e[4])
    print("******************************************************************")

def studentlistbycourse():

    course =input("enter course name: ")
    print("************************student detail***************************")
    for e in list:
        if e[4] == course:
            
            print(e[0] + " | " + e[1])
    print("******************************************************************")

def Qnumber():
    q_number = input("enter qnumber: ")
    print("************************student detail***************************")
    for e in list:
        if e[0] == q_number:
            print(e[1] + " | " + e[2] + " | " + str(e[3]) + " | " + e[4])
    print("******************************************************************")

def change_name():
    Q_number = input("enter q number: ")
    new_name = input("enter new name: ")
    for e in list:
        if e[0]== Q_number:
            e[1] = new_name


while True:
    print("1.add new student ")
    print("2.disply student detail")
    print("3.student detail by course name")
    print("4.Qnumber")
    print("5.chnage name")
    print("0:exit")

    input_number = input("enter number: ")

    match input_number:
        case '1':
            add_student_detail()
        case '2':
            disply()
        case '3':
            studentlistbycourse()
        case '4':
            Qnumber()
        case '5':
            change_name()
        case '0':
            break
