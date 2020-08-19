n = int(input())
k = int(input())
lst = list(map(int, input().split()[:n]))
b = int(input("Enter the value to be paid: "))
sum = 0
for i in range(n):
    if i != k:
        sum += lst[i]
if sum/2 == b:
    print("Bon Appetit")
else:
    print(b-sum/2)