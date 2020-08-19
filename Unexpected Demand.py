n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
k = int(input())
arr.sort()
c = 0
for i in range(len(arr)):
    if k >= arr[i]:
        k -= arr[i]
        c += 1
    else:
        break
print(c)