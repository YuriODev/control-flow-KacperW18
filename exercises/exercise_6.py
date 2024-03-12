# Your solution to Exercise 6
XofA = abs(int(input()))
YofA = abs(int(input()))
XofB = abs(int(input()))
YofB = abs(int(input()))
lengthA = (XofA**2 + YofA**2)**(0.5)
lengthB = (XofB**2 + YofB**2)**(0.5)
if lengthA > lengthB:
    print("A is further from the origin.")
elif lengthA < lengthB:
    print("B is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")