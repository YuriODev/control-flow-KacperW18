# Your solution to Exercise 16
day = int(input())
month = int(input())
year = int(input())
isleap = year % 4 == 0 and (year % 100 != 0 or year % 400 != 0)
if month == 12 or month == 5 or month == 7 or month == 10:
    if day == 1:
        day = 30
        month -= 1
    else:
        day -= 1
elif month == 3:
    if isleap:
        if day == 1:           
            day = 29
            month -= 1
        else:          
            day -= 1
    else:
        if day == 1:
            day = 28
            month -= 1
        else:
            day -= 1
elif month == 12 or month == 4 or month == 6 or month == 8 or month == 9 or month == 11 or month == 2:
    if day == 1:
        day = 31
        month -= 1
    else:
        day -= 1
elif month == 1:
    if day == 1:
        day = 31
        month = 12
        year -= 1
    else:
        day -= 1


output = f"{day:02d}.{month:02d}.{year}"
print(output)
