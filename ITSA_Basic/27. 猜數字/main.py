ans = input()

num = input()
while (num != '0000'):
    a = 0
    b = 0

    for i in range(4):
        if (num[i] == ans[i]):
            a += 1
        else:
            if (ans.count(num[i])):
                b += 1
    
    print(f'{a}A{b}B')

    num = input()