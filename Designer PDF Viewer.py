h = list(map(int, input().split()[:26]))
word = input()
max = 1
for i in word:
    x = ord(i)-97
    if max < h[x]:
        max = h[x]
print(max*len(word))