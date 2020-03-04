n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))
c = 0
ar = [int(ar) for ar in input().split()]
for i in range(0, n):
    for j in range(i+1, n):
        if (ar[i]+ar[j])%k==0:
            c += 1
print("Count = "+str(c))