while True:
    try: # ZeroJudge使用While True必須搭配try, except來進行結束偵測，否則會出現被監控的錯誤訊息，在UVA提交則不需要
        num = list(map(int, input().split()))
        Len, num = num[0], num[1:]

        subtract = []
        for i in range(1, Len):
            subtract.append(abs(num[i] - num[i-1]))
        
        check = True
        subtract.sort()
        for i in range(1, Len):
            if (i not in subtract):
                check = False
                break
        
        if check:
            print('Jolly')
        else:
            print('Not jolly')
    
    except:
        break