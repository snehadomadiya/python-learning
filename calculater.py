

def plus():
    dis(A + B)

def dis(out):
    print("------------Out Put-------------")
    print(out)
    print("-------------------------------")


def minus():
    dis(A - B)

def multiply():
    dis(A * B)

def divide():
    dis(A / B)



while True:
    print("1.plus value")
    print("2.minus value")
    print("3.multiply value")
    print("4.divide value")
    print("5.break")

    input_value = input("Choise a number: ")

    A = int(input("Enter value a: "))
    B = int(input("Enter value b: "))

    
    match input_value:
        case '1':
            plus()
        case '2':
            minus()
        case '3':
            multiply()
        case '4':
            divide()
        case '5':
            break