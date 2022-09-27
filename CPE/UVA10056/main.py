import math

t = int(input())

for i in range(t):
    n, p, i = map(float, input().split())

    ans = (math.pow((1 - p), (i - 1)) * p) * (1 / (1 - math.pow((1 - p), n)))
    print("%.4f"%round(ans, 4))