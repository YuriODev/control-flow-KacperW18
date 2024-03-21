# Your solution to Exercise 13
number = int(input())
num1 = number // 1000
num2 = number // 100 % 10
num3 = number // 10 % 10
num4 = number % 10
if num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
    print("False")
else:
    print("True")