n = int(input("Enter the number of integers in the array: "))
arr = [int(arr) for arr in input().split()]
d = int(input("Enter the day of the birthday: "))
m = int(input("Enter the month of the birthday: "))
sum = 0
c = 0
for i in range(0, n-m+1):
    sum = 0
    for j in range(i, i+m):
        sum = sum + arr[j]
    if sum == d:
        c += 1
print(c)