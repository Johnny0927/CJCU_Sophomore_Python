num = int(input())

if (num >= 0):
    temp = bin(num).replace("0b", "").zfill(8)

    print(temp)
else:
    temp = (num*-1)-1
    temp = bin(temp).replace("0b", "").zfill(8)
    temp = temp.replace("1", "2").replace("0", "1").replace("2", "0")

    print(temp)
