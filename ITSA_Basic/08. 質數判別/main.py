num = int(input())

check = False
for i in range(2, ((num//2)+1)):
    if ((num % i) == 0):
        check = True
        break

if check:
    print('NO')
else:
    print('YES')