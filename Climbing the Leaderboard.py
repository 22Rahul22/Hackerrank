n = int(input("Enter number of players: "))
scores = list(map(int, input().split()[:n]))
m = int(input("Enter the number if games Alice plays: "))
alice = list(map(int, input().split()[:n]))
a = []
b = []
c = []
for i in scores:
    if i not in a:
        a.append(i)
b = alice + a
b.sort(reverse=1)
print(b)
print(a)
for i in range(m):
    x = b.index(alice[i])
    s = x-(m-1-i)+1
    c.append(s)
print(alice)
print(c)