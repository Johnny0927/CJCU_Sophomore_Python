money, apple, orange, peach = list(map(int, input().split(',')))

money -= ((apple*15) + (orange*20) + (peach*30))

if(money < 0):
    print('0')
else:
    change = [] # 找零數量
    for i in [50, 5, 1]:
        change.append(str(money//i))
        money %= i

    print(','.join(change[::-1]))