n = int(input())
x = {}
for _ in range(n):
    s = input().split(" ")
    x[s[0]] = s[1]
while True:
    s = input()
    if s == "":
        break
    if s in x:
        print(s+"="+x[s])
    else:
        print("Not found")