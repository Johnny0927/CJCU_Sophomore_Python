while True:
    try:
        s, d = map(int, input().split())

        while(d > 0):
            d -= s
            s += 1

        print(s-1)
    except:
        break