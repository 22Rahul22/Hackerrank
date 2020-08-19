
y = int(input())
print(y)
if 1700 <= y <= 1918:
    if y % 4 == 0:
        print("12.09."+str(y))
    else:
        print("1")
elif 1919 <= y <= 2700:
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        print("12.09."+str(y))
    else:
        print("13.09."+str(y))