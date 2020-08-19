s = input("Enter the original string: ")
t = input("Enter the required string: ")
k = int(input("Enter the number of operations: "))
a = list(s)
b = list(t)
x = len(a)
y = len(b)
if a == b:
    print("YES")
else:
    if y+x < k:
        print("YES")
    else:
        for i in range(min(x,y)):
            if a[i] != b[i]:
                break
        if x+y-2*i > k:
            print("NO")
        else:
            print("YES")


