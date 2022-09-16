while True:
    r, c = map(int, input().split())

    matrix = []

    for i in range(r):
        now_r = list(map(int, input().split()))
        matrix.append(now_r)

    for i in range(c):
        output = []
        for j in range(r):
            output.append(str(matrix[j][i]))
        print(" ".join(output))