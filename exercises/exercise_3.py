# Your solution to Exercise 3
number = int(input())
output = ""
if number == 0:
    output = "Green"
elif number < 11 or (number > 29 and number < 36) and number % 2 != 0:
    output = "Red"
elif number < 11 or (number > 29 and number < 36) and number % 2 == 0:
    output = "Black"
elif number > 19 and number < 29 and number % 2 == 0:
    output = "Black"
elif number > 19 and number < 29 and number % 2 != 0:
    output = "Red"
else:
    output = "The bet will not play!"
print (output)