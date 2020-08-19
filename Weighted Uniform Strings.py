s = input()
al = 'abcdefghijklmnopqrstuvwxyz'
q = int(input())
a = []
j = 0
a.append(al.index(s[0])+1)
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        a.append(al.index(s[i]) + a[j]+1)
        j += 1
    else:
        a.append(al.index(s[i])+1)
        j += 1
for _ in range(q):
    n = int(input())
    if n in a:
        print("Yes")
    else:
        print("No")
