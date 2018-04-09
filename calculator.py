def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Test Calculator")



while True:
    x = int(input("Enter number:"))
    operator = input("Enter operator (+, -, *, /):")
    y = int(input("Enter number:"))
    if operator == "+":
        print(add(x, y))
        print("if you would like to exit type e or if you would like to continue, type c.")
        answer = input()
        if answer == 'e':
            break

    elif operator == "-":
        print(subtract(x, y))
        print("if you would like to exit type e or if you would like to continue, type c.")
        answer = input()
        if answer == 'e':
            break

    elif operator == "*":
        print(multiply(x, y))
        print("if you would like to exit type e or if you would like to continue, type c.")
        answer = input()
        if answer == 'e':
            break

    elif operator == "/":
        print(divide(x, y))
        print("if you would like to exit type e or if you would like to continue, type c.")
        answer = input()
        if answer == 'e':
            break

    else:
        print("Error, try again")
