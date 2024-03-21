# Your solution to Exercise 12
number = int(input())
num1 = number // 1000
num2 = (number // 100) % 10
num3 = (number // 10) % 10
num4 = number % 10
if num1 % 2 == 0:
    num1 = "*"
if num2 % 2 == 0:
    num2 = "*"
if num3 % 2 == 0:
    num3 = "*"
if num4 % 2 == 0:
    num4 = "*"
newnum = str(num1) + str(num2) + str(num3) + str(num4)
print(newnum)
    

