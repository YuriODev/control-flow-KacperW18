# Your solution to Exercise 1
alex_age = int(input())
Tatyana = int(input())
output = ""
if alex_age > Tatyana:
    output = "Alex is the eldest."
if Tatyana > alex_age:
    output = "Tatyana is the eldest."
else:
    output = "Alex and Tatyana are the same age."
print(output)