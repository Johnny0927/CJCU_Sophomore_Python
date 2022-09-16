times = int(input())

for i in range(times):
    cards = list(input().split())

    card_suits = {'S':[], 'H':[], 'D':[], 'C':[]}

    for j in cards:
        card_suits[j[0]].append(int(j[1:]))

    for j in card_suits.keys():
        card_suits[j] = sorted(card_suits[j], reverse=True) # 數字大的要在前，所以要反轉(reverse)

    result = []
    for j in ['S', 'H', 'D', 'C']: # suit 大到小依序
        for k in card_suits[j]:
            result.append(f'{j}{k}')
    
    print(' '.join(result))