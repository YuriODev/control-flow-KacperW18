# Your solution to Exercise 10
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

adj = ((abs(x1 - x2)**2)+(abs(y1 - y2)**2))**0.5
opp = ((abs(x1 - x3)**2)+(abs(y1 - y3)**2))**0.5
hyp = ((abs(x2 - x3)**2)+(abs(y2 - y3)**2))**0.5
realhyp = (adj**2 + opp**2)**0.5

if x1 == x2 == x3 or y1 == y2 == y3:
    print("No")
elif realhyp == hyp:
    print("Yes")
else:
    print("No")