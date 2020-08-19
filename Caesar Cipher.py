n = int(input())
s = input()
k = int(input())
k = k % 26
a = ''
for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        if ord(i) + k > 122:
            a += chr(ord(i) + k - 26)
        elif 65 <= ord(i) <= 90 and (ord(i) + k) > 90:
            a += chr(ord(i) + k - 26)
        else:
            a += chr(ord(i) + k)
    else:
        a += i
print(a)