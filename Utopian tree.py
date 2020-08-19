t = int(input())
while(t > 0):
    n = int(input())
    height = 1
    if n == 0:
        print(height)
    else:
        for i in range(1,n+1):
            if i % 2 == 0:
                height += 1
            else:
                height *= 2
        print(height)
    t -= 1