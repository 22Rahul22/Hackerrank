n = int(input("Enter the number of integers to be inserted: "))
arr = [int(arr) for arr in input().split()]
maxi = 0
mini = 0
max = arr[0]
min = arr[0]
for i in range(0,n-1):
    if max<arr[i+1]:
        max = arr[i+1]
        maxi += 1
    if min>arr[i+1]:
        min = arr[i+1]
        mini += 1
print(maxi)
print(mini)
