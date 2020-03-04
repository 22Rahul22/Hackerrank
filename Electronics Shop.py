b = int(input("Enter the budget: "))
n = int(input("Enter the no. of Keyboards: "))
m = int(input("Enter the number of USB: "))
keyboard = list(map(int, input().split()[:n]))
drives = list(map(int, input().split()[:m]))
keyboard.sort(reverse=1)
drives.sort(reverse=1)
flag = 0
c = []
a = 0
print(keyboard)
print(drives)
for i in range(len(keyboard)):
    if keyboard[i] <= b:
        break
for j in range(len(drives)):
    if drives[j] <= b:
        break
for k in range(i,len(keyboard)):
    for z in range(j,len(drives)):
        if keyboard[k] + drives[z] == b:
            a = (keyboard[k]+drives[z])
            flag = 1
            break
        elif keyboard[k] + drives[z] < b:
            flag = 1
            c.append(keyboard[k] + drives[z])
c.sort(reverse=1)
if flag == 1 and c[0] < a:
    print(a)
elif flag == 1 and c[0] > a:
    print(c[0])
else:
    print(-1)