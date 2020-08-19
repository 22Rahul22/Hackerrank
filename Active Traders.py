n = int(input())
customers = []
a = []
z = []
for i in range(n):
    s = input()
    customers.append(s)
customers.sort()
c = 0
for i in range(n-1):
    if customers[i] == customers[i+1]:
        c += 1
    else:
        c += 1
        if c / n * 100 >= 5:
            a.append(customers[i])
        c = 0
if c / n * 100 >= 5:
    a.append(customers[n-1])
for i in range(len(a)):
    print(a[i])