import math
n = int(input())
x = 5
sum = 2
if n == 1:
    print(sum)
else:
    for i in range(2,n+1):
        x = math.floor(x/2) * 3
        sum += math.floor(x/2)
    print(sum)