english_convert = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'J': 18, 'K': 19,
    'L': 20, 'M': 21, 'N': 22, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29,
    'X': 30, 'Y': 31, 'W': 32, 'Z': 33, 'I': 34, 'O': 35
    }

num = input()

total = 0

num_of_english = str(english_convert[num[0]])
total += (int(num_of_english[0]) + (int(num_of_english[1]) * 9))

for i in range(1, 10):
    multiple = (9 - i)
    if (multiple > 1):
        total += (int(num[i]) * multiple)
    else:
        total += int(num[i])

if ((total % 10) == 0):
    print('CORRECT!!!')
else:
    print('WRONG!!!')