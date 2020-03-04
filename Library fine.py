d1, m1, y1 = [int(d1) for d1 in input().split()]
d2, m2, y2 = [int(d2) for d2 in input().split()]
fine = 0
if y1 == y2:
    if m1 == m2:
        if d1 > d2:
            fine = 15 * (d1-d2)
    elif m1 > m2:
        fine = 500 * (m1-m2)
elif y1 > y2:
    fine = 10000
print(fine)