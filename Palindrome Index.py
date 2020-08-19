q = int(input())
for _ in range(q):
    s = input()
    i = 0
    j = len(s) - 1
    flag = 0
    while i <= j:
        if s[i] != s[j] and s[i + 1] == s[j] and s[i + 2] == s[j - 1]:
            flag = 1
            print(i)
            break
        elif s[i] != s[j] and s[j - 1] == s[i]:
            print(j)
            flag = 1
            break
        else:
            i += 1
            j -= 1
    if flag == 0:
        print(-1)
