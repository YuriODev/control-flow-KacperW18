# Your solution to Exercise 4
grade = int(input())
if grade <= 3:
    print("initial level")
elif grade <= 6:
    print("average level")
elif grade <= 9:
    print("sufficient level")
elif grade <= 12:
    print("high level")
else:
    print("level is absent")
