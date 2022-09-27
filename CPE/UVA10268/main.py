import math
while True:
    try:
        x = int(input())

        a = list(map(int, input().split()))

        del a[-1] # 微分後不會有常數位，提早拿掉可以讓後續for迴圈內的(len(a)-i)剛好是對應的x次方
        for i in range(len(a)):
            a[i] *= (len(a) - i)

        total = 0
        for i in range(len(a)):
            total += (a[i] * math.pow(x, (len(a) - i - 1)))

        print(int(total))
    except:
        break