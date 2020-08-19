def minimum(n, m):
    f = [int(i) for i in input().split()[:n]]
    p = [int(i) for i in input().split()[:n]]
    arr = list()
    for j in range(m):
        arr.append(0)
    for j in range(n):
        arr[f[j] - 1] += p[j]
    min = 100
    for j in arr:
        if j < min and j != 0:
            min = j
    return min
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        result = minimum(n, m)
        print(result)
