def draw_number(number):
    if (number == 0):
        return [
            "*****",
            "*   *",
            "*   *",
            "*   *",
            "*****"
            ]
    elif (number == 1):
        return [
            "    *",
            "    *",
            "    *",
            "    *",
            "    *"
            ]
    elif (number == 2):
        return [
            "*****",
            "    *",
            "*****",
            "*    ",
            "*****"
            ]
    elif (number == 3):
        return [
            "*****",
            "    *",
            "*****",
            "    *",
            "*****"
            ]
    elif (number == 4):
        return [
            "*   *",
            "*   *",
            "*****",
            "    *",
            "    *"
            ]
    elif (number == 5):
        return [
            "*****",
            "*    ",
            "*****",
            "    *",
            "*****"
            ]
    elif (number == 6):
        return [
            "*****",
            "*    ",
            "*****",
            "*   *",
            "*****"
            ]
    elif (number == 7):
        return [
            "*****",
            "    *",
            "    *",
            "    *",
            "    *"
            ]
    elif (number == 8):
        return [
            "*****",
            "*   *",
            "*****",
            "*   *",
            "*****"
            ]
    elif (number == 9):
        return [
            "*****",
            "*   *",
            "*****",
            "    *",
            "    *"
            ]

num = input()
draw = []

for i in num:
    draw.append(draw_number(int(i)))

output = []

for i in range(5):
    output.append([])
    for j in range(len(draw)):
        output[i].append(draw[j][i])

for i in output:
    print(" ".join(i)) # 每行最後不能有空白，因此用 join 可以不需要另外處理