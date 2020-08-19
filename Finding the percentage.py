n = int(input())
d = {}
for i in range(n):
    a = input().split(" ")
    s = a[0]
    arr = a[1:]
    d[s] = map(float, arr)
q = input()
arr = d[q]
s = sum(arr)
print('%.2f'%(s/3))
