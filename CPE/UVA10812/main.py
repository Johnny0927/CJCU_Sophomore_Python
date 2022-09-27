t = int(input())

for i in range(t):
    s, d = map(int, input().split())
    
    s1 = int(((s - d) / 2) + d)
    s2 = s1 - d

    if ((s1 + s2) == s) and (s1 >= 0 <= s2):
        print(s1, s2)
    else:
        print('impossible')