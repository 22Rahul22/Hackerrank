t = int(input())
b = []
for _ in range(t):
    a = input().split()
    s = a[0]
    arr = a[1:]
    if s == 'insert':
        b.insert(int(arr[0], 10), int(arr[1], 10))
    elif s == 'print':
        print(b)
    elif s == 'append':
        b.append(arr[0])
    elif s == 'remove':
        b.remove(arr[0])
    elif s == 'sort':
        b.sort()
    elif s == 'pop':
        b.pop()
    else:
        b.reverse()
