n = int(input("Enter the number of hurdles: "))
k = int(input("Enter the height Dan can jump: "))
print("Enter the height of the hurdles: ")
height = list(map(int, input().split()[:n]))
max = height[0]
for i in height:
    if i > max:
        max = i
pos = max - k
if pos < 0:
    print("0")
else:
    print(pos)
