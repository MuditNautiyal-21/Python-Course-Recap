try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("Please select the operation you want to perform:\n1. Press '+' for addition\n2. Press '-' for subtraction\n3. Press '*' for multiplication\n4. Press '/' for division")

    op = input("Enter your choice: ")

    match op:
        case "+":
            print(f"The result of {a} + {b} is: {a + b}")
        case "-":
            print(f"The result of {a} - {b} is: {a - b}")
        case "*":
            print(f"The result of {a} * {b} is: {a * b}")
        case "/":
            if b != 0:
                print(f"The result of {a} / {b} is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case default:
            print("Invalid operation selected. Please choose +, -, *, or /.")
except Exception as e:
    print("Enter a valid value please.")