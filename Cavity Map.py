n = int(input())
a = []
b = []
for i in range(n):
    x = int(input())
    a.append([int(d) for d in str(x)])
for i in range(0, n):
    for j in range(0, n):
        if n - 1 > i > 0 and n-1 > j > 0:
            if a[i][j] > a[i - 1][j] and a[i][j] > a[i + 1][j] and a[i][j] > a[i][j - 1] and a[i][j] > a[i][j + 1]:
                print('X',end="")
            else:
                print(a[i][j], end="")
        else:
            print(a[i][j],end="")
    print()

