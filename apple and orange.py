s, t = [int(s) for s in input().split()]
a, b = [int(a) for a in input().split()]
c1 = 0
c2 = 0
m, n = [int(m) for m in input().split()]
apple = [int(apple) for apple in input().split()]
orange = [int(orange) for orange in input().split()]
for i in range(0, m):
    apple[i] = apple[i] + a
    if s <= apple[i] <= t:
        c1 += 1
for i in range(0, n):
    orange[i] = orange[i] + b
    if s <= orange[i] <= t:
        c2 += 1
print(apple)
print(orange)
print(c1)
print(c2)
