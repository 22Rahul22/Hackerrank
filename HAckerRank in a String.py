t = int(input())
for _ in range(t):
    h = 'hackerrank'
    s = input()
    j = 0
    for i in range(len(s)):
        if s[i] == h[j]:
            j += 1
            if j == len(h):
                break
    if j == len(h):
        print("YES")
    else:
        print("NO")