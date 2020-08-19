n = int(input())
arr = list(map(int, input().split()[:n]))
b = []
for i in range(n):
    k = i+1
    b.append(1)
    for j in range(k,n):
        if arr[i] == arr[j]:
            b[i] += 1
print(n-max(b))
