# function for addition
def add(num1, num2):
    return num1 + num2

# function for subtraction
def subtract(num1, num2):
    return num1 - num2

# function for multiplication
def multiply(num1, num2):
    return num1 * num2

# function for division
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

# main program
while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid input")
