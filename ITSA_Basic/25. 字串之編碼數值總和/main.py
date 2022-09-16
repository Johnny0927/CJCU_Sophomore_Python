# 本題的空格也需要計算到total內
times = int(input())

for t in range(times):
    sentence = input()
    total = 0
    for i in sentence:
        total += ord(i)

    print(total)