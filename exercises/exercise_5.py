# Your solution to Exercise 5
a = float(input())
b = float(input())
c = float(input())

if a == b == c == 0:
    print("Infinite roots.")
    
elif a == 0 and b != 0 and c != 0:
    print(c/b)
    
elif a == 0 and b == 0 and c != 0:
    print("No roots.")
    
else:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("No roots.")
        
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        
        if root1 == root2:
            print(root1)
            
        else:
            print(root1,"and",root2)
