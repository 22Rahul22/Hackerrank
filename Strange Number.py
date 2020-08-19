import math


def isPrime(a):
    for i in range(int(math.sqrt(a))):
        if a % i == 0:
            return 0


t = int(input())
while t > 0:
    x = int(input())
    k = int(input())
    a = []
    t -= 1
    print(isPrime(x))
