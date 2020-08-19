n = int(input("Enter the number of socks in the pile: "))
ar = list(map(int, input().split()[:n]))
a = []
b = []
sum = 0
for i in ar:
    if i not in a:
        a.append(i)
for i in range(len(a)):
    b.append(0)
    b[i] = ar.count(a[i])
for i in range(len(b)):
    a[i] = b[i]/2
    if a[i] - int(a[i]) == 0:
        sum += a[i]
    else:
        sum += a[i]-0.5
print(a)
print(b)
print(ar)
print(sum)
