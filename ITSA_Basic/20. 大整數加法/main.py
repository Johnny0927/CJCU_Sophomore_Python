# 要做加法會有進位問題，因此從個位數開始會比較方便，一開始先將兩數值轉到陣列內，並由個位數開始放

times = int(input())

for t in range(times):
    num = input().split() # 整數過大，不能使用 int 儲存
    
    num1, num2 = [], []
    long_len = max(len(num[0]), len(num[1]))
    for i in range(-1, ((long_len * -1)-1), -1): # 將兩個數值放到陣列，並從個位數開始放
        if ((len(num[0]) * -1) <= i):
            num1.append(num[0][i])
        else:
            num1.append('0')

        if ((len(num[1]) * -1) <= i):
            num2.append(num[1][i])
        else:
            num2.append('0')

        # 123456    => ['6', '5', '4', '3', '2', '1', '0', '0', '0']
        # 123456789 => ['9', '8', '7', '6', '5', '4', '3', '2', '1']

    result = ''
    carry = False # 紀錄該位數是否進位
    for i in range(long_len):
        now_num = int(num1[i]) + int(num2[i])
        if carry:
            now_num += 1

        if (now_num >= 10):
            carry = True
            now_num %= 10
        else:
            carry = False

        result += str(now_num)

    if carry:
        result += '1'
    
    print(result[::-1])