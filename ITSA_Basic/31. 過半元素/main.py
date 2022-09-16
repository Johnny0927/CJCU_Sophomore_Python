while True:
    num = list(map(int, input().split()))

    check = False
    num_set = set(num)
    for i in num_set:
        if (num.count(i) > (len(num) // 2)):
            print(i)
            check = True

    if not check:
        print('NO')