from collections import Counter
n = int(input("Enter the size of the array: "))
a = list(map(int, input().split()[:n]))
b = []
c = []
a.sort()
m = 0
i = 0
for i in a:
    if i not in b:
        b.append(i)
for i in range(len(b)):
    c.append(0)
    c[i] = a.count(b[i])
m = max(c)
if len(c) == 1:
    print(n)
else:
    for i in range(len(c)-1):
        if m <= c[i] + c[i+1] and abs(b[i] - b[i+1]) <= 1:
            m = c[i] + c[i+1]
    print(m)
print(b)
print(c)
