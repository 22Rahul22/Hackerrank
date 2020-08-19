def calculate(arr, k):
    c = {}
    s = k
    for i in range(len(arr)):
        if arr[i] not in c:
            c[arr[i]] = 1
        else:
            c[arr[i]] += 1
    for i in c:
        if c[i] > 1:
            s += c[i]
    return s


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    a = []
    b = []
    i = 0
    while i < len(arr):
        b = []
        for j in range(i, len(arr)):
            if arr[j] not in b:
                b.append(arr[j])
                i += 1
            else:
                a.append(b)
                break
    if len(b) != 0:
        a.append(b)
    i = 0
    j = 1
    while j < len(a):
        sum1 = calculate(a[i], k)
        sum2 = calculate(a[j], k)
        ts = sum1 + sum2
        tsn = sum1
        m = a[i].copy()
        n = a[j].copy()
        h = 0
        while tsn != ts - 1 and n:
            m.append(n[h])
            n.remove(n[h])
            tsn = calculate(m, k)
            if n:
                e = calculate(n, k)
            else:
                e = 0
            if ts < tsn+e:
                n.insert(0,m[len(m)-1])
                m = m[:len(m)-1]
                break
        a[i] = m
        if n:
            a[j] = n
            i += 1
            j += 1
        else:
            a.remove(a[j])
    ans = 0
    print(a)
    for i in range(len(a)):
        ans += calculate(a[i], k)
    print(ans)
