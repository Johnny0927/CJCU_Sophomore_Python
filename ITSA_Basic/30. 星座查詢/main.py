constellation = {
    'Aquarius': [[1, 21], [2, 18]],
    'Pisces': [[2, 19], [3, 20]],
    'Aries': [[3, 21], [4, 20]],
    'Taurus': [[4, 21], [5, 21]],
    'Gemini': [[5, 22], [6, 21]],
    'Cancer': [[6, 22], [7, 22]],
    'Leo': [[7, 23], [8, 23]],
    'Virgo': [[8, 24], [9, 23]],
    'Libra': [[9, 24], [10, 23]],
    'Scorpio': [[10, 24], [11, 22]],
    'Sagittarius': [[11, 23], [12, 21]],
    'Capricorn': [[12, 22], [1, 20]]
    }

m, d = list(map(int, input().split()))

for i in constellation.keys():
    if ((m == constellation[i][0][0]) and (d >= constellation[i][0][1])) or ((m == constellation[i][1][0]) and (d < constellation[i][1][1])):
        print(i)