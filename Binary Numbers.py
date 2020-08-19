n = int(input())
b = bin(n).replace("0b", "");
c = 0
m = 0
for i in range(len(b)):
    if b[i] == '1':
        c += 1
    else:
        if c > m:
            m = c
        c = 0
if c > m:
    m = c
print(m)