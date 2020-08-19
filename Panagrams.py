s = input()
s = s.lower()
a = []
flag = 1
for i in s:
    if i not in a and i != " ":
        a.append(i)
    if len(a) == 26:
        print('pangram')
        flag = 0
        break
if flag == 1:
    print("not pangram")