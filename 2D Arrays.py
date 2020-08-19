arr = [[0 for i in range(6)] for j in range(6)]
for i in range(6):
    arr[i] = list(map(int, input().split()))
sum = 0
a = []
for i in range(4):
    for j in range(1,5):
        sum = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j-1] + arr[i+2][j] + arr[i+2][j+1]
        a.append(sum)
print(max(a))