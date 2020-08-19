n, k = [int(n) for n in input().split()]
c = 0
while n > 0:
    t = int(input())
    if t % k == 0:
        c += 1
    n -= 1
print(c)