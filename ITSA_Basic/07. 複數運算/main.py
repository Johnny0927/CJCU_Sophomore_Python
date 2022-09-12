n = int(input())  
for i in range(n):
    w,a1,a2,b1,b2 = map(str,input().split())

    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)

    if (w == '+'):
        print((a1 + b1), (a2 + b2))
    elif (w == '-'):
        print((a1 - b1), (a2 - b2))
    elif (w == '*'):
        print(((a1 * b1) - (a2 * b2)), ((a2 * b1) + (a1 * b2)))
    else:
        print((((a1 * b1) + (a2 * b2)) / ((b1 * b1) + (b2 * b2))), (((a2 * b1) - (a1 * b2)) / ((b1 * b1) + (b2 * b2))))