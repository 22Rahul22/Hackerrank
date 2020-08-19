import math
q = int(input())
for _ in range(q):
    s = input()
    i = 0
    j = len(s)-1
    c = 0
    while i < j:
        if ord(s[i]) >= ord(s[j]):
            c += ord(s[i]) - ord(s[j])
            i += 1
            j -= 1
        elif ord(s[i]) <= ord(s[j]):
            c += ord(s[j]) - ord(s[i])
            i += 1
            j -= 1
    print(c)