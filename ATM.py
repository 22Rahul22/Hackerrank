x, y = [float(x) for x in input().split()]
if x < y:
    if x % 5 == 0:
        print('%.2f' % (y - x - 0.5))
    else:
        print('%.2f' % y)
else:
    print('%.2f' % y)
