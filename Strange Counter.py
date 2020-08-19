t = int(input())
x = 3
y = 1
z = 0
a = True
while a:
    z = x + y
    if y <= t < z:
        break
    else:
        y += x
    x *= 2
print(x-abs(t-y))