times = int(input()) # 本題若用 Python 則不需要次數

num = list(input().split())

num_total = {}
for i in num:
    now_total = 0
    for j in i:
        now_total += int(j)
    
    if (now_total not in num_total):
        num_total[now_total] = [int(i)]
    else:
        num_total[now_total].append(int(i))

result = []
total_sort = sorted(num_total)
for i in total_sort:
    now = sorted(num_total[i])
    for j in now:
        result.append(str(j))

print(' '.join(result))
