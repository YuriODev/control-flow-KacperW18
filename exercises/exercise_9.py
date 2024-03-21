# Your solution to Exercise 9
number = int(input())
num1 = number // 100
num2 = number // 10 % 10
num3 = number % 10
total = num1 + num3
if total == num2:
    print("=")
elif total > num2:
    print(">")
else:
    print("<")
