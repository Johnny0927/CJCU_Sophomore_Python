r = float(input())
n = int(input())
p = int(input())

money = 0
for i in range(n):
    money += p
    money += (money * r)

print(int(money))