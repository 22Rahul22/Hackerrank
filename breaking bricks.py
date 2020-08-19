t = int(input("Enter the number of test cases: "))
c = 0
z = 0
d = 0
addf = 0
addr = 0

while(t > 0):
    s = int(input("Entert the of strength: "))
    print("Enter the width of the bricks: ")
    w = [int(w) for w in input().split()]
    print(w)
    minm = 0
    d = 0
    maxm = len(w)-1
    for j in range(minm, maxm):
        print("minimum = "+str(minm)+" maximum = "+str(maxm))
        if maxm is minm:
            d += 1
            break
        else:
            i = minm
            k = maxm
            addf = 0
            addr = 0
            c = 0
            z = 0
            while s >=addf and i <maxm:
                addf = addf + w[i]
                i += 1
                c += 1
            while s >= addr and k > minm:
                addr = addr + w[k]
                k -= 1
                z += 1
            if i == k:
                d += 1
                break
            else:
                if c > z:
                    minm = i-1
                else:
                    maxm = k+1
        d += 1
    print(d)
    t -= 1
