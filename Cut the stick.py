n = int(input())
arr = list(map(int, input().split()[:n]))
b = []
c = 0
i = 0
b.append(n)
arr.sort()
print(arr)
while i < n:
    a = arr[i]
    j = 0
    while j < n:
        arr[j] = arr[j] - a
        #print("J ------ "+str(arr[j]))
        if arr[j] == 0:
            arr.remove(0)
            j = 0
        n = len(arr)
        j += 1
    i += 1
    print(arr)