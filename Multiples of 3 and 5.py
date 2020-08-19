t = int(input())
while(t > 0):
    n = int(input())
    x = int(n/3)
    y = int(n/5)
    z = int(n/15)
    if n % 3 == 0 or n % 5 == 0:
        sum = int((3*x*(x+1)/2) + (5*y*(y+1)/2) - (15*z*(z+1)/2)) - n
    else:
        sum = int((3 * x * (x + 1) / 2) + (5 * y * (y + 1) / 2) - (15 *z*(z+1)/2))
    print(sum)
    t -=1