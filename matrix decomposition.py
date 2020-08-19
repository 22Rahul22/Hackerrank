m = pow(10, 9) + 7
print(m)
print(1099511627776 % m)
t = int(input())
for _ in range(t):
    n, a = map(int, input().split())
    e = 2*(n+1)
    print(e)
    p = pow(a, e)
    print(p)
    print(2*n-1)
    ans = pow(p, 2*n-1)
    print(ans)
    print(ans % m)
