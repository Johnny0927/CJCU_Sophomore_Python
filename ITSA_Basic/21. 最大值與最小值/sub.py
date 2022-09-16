num = list(map(float, input().split()))

num = sorted(num)

print(f'maximum:{"%.2f"%num[-1]}')
print(f'minimum:{"%.2f"%num[0]}')