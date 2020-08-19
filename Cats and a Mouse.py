t = int(input("Enter the number of queries: "))
while(t > 0):
    x = int(input("Enter the pos of cat A: "))
    y = int(input("Enter the pos of cat B: "))
    z = int(input("Enter the pos of mouse: "))
    dif1 = abs(x-z)
    dif2 = abs(y-z)
    if dif1 > dif2:
        print("Cat B")
    elif dif1 < dif2:
        print("Cat A")
    else:
        print("Mouse")