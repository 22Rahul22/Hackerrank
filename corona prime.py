import math
def isprime(num):
    for i in range(2,int(num/2)):
        if num % i == 0:
            return 0
        else:
            return 1

t = int(input())
for i in range(t):
    x, y = [int(x) for x in input().split()]
    d = x - y
    flag = 0
    if isprime(d) == 1 or d == 2:
        print("YES")
        flag = 1
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    for k in a:
        if d % k == 0 and flag != 1:
            print("YES")
            flag = 1
            break
    if flag != 1:
        print("NO")