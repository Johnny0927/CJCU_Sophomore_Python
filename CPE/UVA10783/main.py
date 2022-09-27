t = int(input())

for i in range(t):
    a = int(input())
    b = int(input())

    total = 0
    for j in range(a, (b+1)):
        if ((j % 2) == 1):
            total += j

    print(f'Case {i+1}: {total}')