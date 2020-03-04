import os
import sys
def pageCount(n, p):
    x = 0
    x = n - p
    if x >= p:
        print(int(p / 2))
    else:
        if n % 2 != 0:
            return (int(x / 2))
        else:
            return (int(x / 2 + 0.5))


if __name__ == '__main__':
    n = int(input("Enter the number of pages: "))
    p = int(input())
    result = pageCount(n, p)
    print(result)

