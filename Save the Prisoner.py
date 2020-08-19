from numpy.core import long

t = int(input())
while(t>0):
    n, m, s = [int(n) for n in input().split()]
    final = (m % n + (s-1)) % n
    if final == 0:
        final += n
    print(final)
    t -= 1