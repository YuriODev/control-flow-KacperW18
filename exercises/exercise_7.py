# Your solution to Exercise 7
num1 = float(input())
num2 = float(input())
operation = input()

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    if num2 == 0 :
        print("Division by 0!")
    else:
        print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "mod":
    if num2 == 0 :
        print("Division by 0!")
    else:
        print(num1 % num2)
elif operation == "pow":
    print(num1 ** num2)