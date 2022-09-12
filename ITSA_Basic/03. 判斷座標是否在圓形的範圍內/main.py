import math

x, y = list(map(int, input().split()))

r = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) # 計算畢氏定理

if (r <= 100): # <=半徑就代表在圓內
    print('inside')
else:
    print('outside')