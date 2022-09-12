h1, m1 = list(map(int, input().split()))
h2, m2 = list(map(int, input().split()))

t1 = h1*60 + m1
t2 = h2*60 + m2

t = t2 - t1
h = t//60
m = t%60

m //= 30
m += h*2


price = 0

if (m > 8):
    price += ((m-8)*60)
    m -= (m-8)

if (m > 4):
    price += ((m-4)*40)
    m -= (m-4)
    
price += (m*30)

print(price)