n = int(input())
a = []
for i in range(n):
    a.append((input()))
a.sort(key=lambda x: (len(x), x))
for i in a:
    print(i)