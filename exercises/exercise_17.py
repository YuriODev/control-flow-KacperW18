# Your solution to Exercise 17
number = int(input())
num1 = number // 100000
num2 = number // 10000 % 10
num3 = number // 1000 % 10
num4 = number // 100 % 10
num5 = number // 10 % 10
num6 = number % 10
if num1 + num2 + num3 == num4 + num5 + num6:
    print("Happy")
else:
    print("Ordinary")
