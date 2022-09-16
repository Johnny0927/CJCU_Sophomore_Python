matrix = []
for i in range(3):
    matrix.append(list(input().split()))

check = False
for i in range(3):
    if (matrix[i][0] == matrix[i][1] == matrix[i][2]): # 判斷同行有沒有相同的
        check = True
        break

    elif (matrix[0][i] == matrix[1][i] == matrix[2][i]): # 判斷同列有沒有相同的
        check = True
        break

if (matrix[0][0] == matrix[1][1] == matrix[2][2]) or (matrix[0][2] == matrix[1][1] == matrix[2][0]): # 判斷兩斜線是否相同
        check = True

print(check)