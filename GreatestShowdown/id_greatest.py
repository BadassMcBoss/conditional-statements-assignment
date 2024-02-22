x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

if x == y > z or x == z > y or y == z > x:
    print("Two numbers are equal and the largest!")
elif x == y == z:
    print("All numbers are equal!")
    
if x > y and x > z:
    print(f"{x} is the greatest!")
elif y > x and y > z:
    print(f"{y} is the greatest!")
elif z > x and z > y:
    print(f"{z} is the greatest!")

if x < y and x < z:
    print(f"{x} is the smallest!")
elif y < x and y < z:
    print(f"{y} is the smallest!")
elif z < x and z < y:
    print(f"{z} is the smallest!")