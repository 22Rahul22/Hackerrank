n = int(input())
k = int(input())
c = list(map(int, input().split()[:n]))
flag = True
i = 0
e = 100
while flag:
    x = c[(i+k)%n]
    i = (i+k)%n
    e -= 1
    if x == 1:
       e -= 2
    if i == 0:
        flag = False
print(e)