i = int(input())
j = int(input())
k = int(input())
c = 0
for x in range(i,j+1):
    temp = x
    n = 0
    while(temp > 0):
        r = temp % 10
        n = n*10 + r
        temp = temp//10
    n = abs(n-x)
    if n % k == 0:
        c += 1
print(c)