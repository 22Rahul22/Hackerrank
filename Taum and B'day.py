t = int(input())
while t > 0:
    b, w = [int(b) for b in input().split()]
    bc, wc, z = [int(bc) for bc in input().split()]
    cost = 0
    if bc > wc + z:
        cost = w * wc + b * (wc+z)
    elif wc > bc + z:
        cost = b * bc + w * (bc+z)
    else:
        cost = b * bc + w * wc
    print(cost)
    t -= 1
