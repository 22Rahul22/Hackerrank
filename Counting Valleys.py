n = int(input("Enter the number of steps: "))
s = input("Enter the ups and downs: ")
print(s)
sea = 0
c = 0
for i in range(n):
    if s[i] == 'D':
        sea -= 1
    else:
        sea += 1
        if sea == 0:
            c += 1
print(c)
