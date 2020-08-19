import math
n = int(input())
arr = list(map(int, input().split()[:n]))
arr.sort()
print(arr[math.floor(n/2)])