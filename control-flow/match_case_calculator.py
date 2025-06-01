num1 = int(input("Enter the first number: " ))
num2 = int(input("Enter the second number: "))
calculator = input("Choose the operation (+, -, *, /): ")
match calculator:
    case "+":
        result = (num1 + num2)
    case "-":
        result = (num1 - num2)
    case "*":
        result = (num1 * num2)
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = (num1 / num2)
print(f"The result is {result}.")