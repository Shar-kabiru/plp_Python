num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
    
operation = input("Enter the operation (+, -, *, /): ")
    
if operation == '+':
        result = num1 + num2
elif operation == '-':
        result = num1 - num2
elif operation == '*':
        result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        
else:
    print("Error: Invalid operation.")

    
    # Print the result
print(f"The result of {num1} {operation} {num2} is: {result}")