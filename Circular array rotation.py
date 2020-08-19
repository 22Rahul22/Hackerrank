n = int(input())
k = int(input())
q = int(input())
b = list(map(int,input().split()[:n]))
print(len(b))
a = list(map(int,input().split()))
for i in a:
    x = (n-k+i) % n
    print(b[x])
