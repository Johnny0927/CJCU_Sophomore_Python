n = int(input())

Time = list(map(int, input().split()))

start = [] # 車輛出去的時間點
end = [] # 車輛回來的時間點
for i in range(len(Time)): # 將車輛出去跟回來的時間點先分類
    if((i % 2) == 0):
        start.append(Time[i])
    else:
        end.append(Time[i])

num_of_car = [] # 儲存每個時段需要幾台車(第一個位置是1點，最後一個位置是23點)

car = 0 # 初始車輛為0，因為還沒有任何一台車出去
now = 0 # 出使時間為0點
while (now <= 23):
    now = now + 1 # 目前時間(1, 2, 3, 4, ..., 23)，題目有告知不會有0跟24點(0 < si < di ≤ 24)
    
    car += start.count(now) # 這小時有幾台車出發，就加多少
    car -= end.count(now) # 這小時有幾台車回來，就減多少

    num_of_car.append(car)

print(max(num_of_car)) # 輸出最大值 = 同時需要車的最大數量