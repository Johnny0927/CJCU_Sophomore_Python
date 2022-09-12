num = int(input())

Sum = 0
for i in range((num+1)):
    if ((i % 3) == 0):
        Sum += i

print(Sum)