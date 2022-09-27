m_to_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_cycle = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# 由測資得到1/6是Thursday，回推1/1是Saturday，因此將Saturday放在第0個元素，若不放第0個則最後需要將日期加到陣列中對應的位置

t = int(input())

for i in range(t):
    m, d = map(int, input().split())
    
    for j in range(m-1):
        d += m_to_d[j]

    print(day_cycle[(d-1)%7])