import math

def f(n):
    if (n == 0) or (n == 1):
        return n+1
    else:
        return f(n-1)+f(math.floor(n/2))

print(f(int(input())))