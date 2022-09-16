words = list(input().split())

print(len(words)) # 字的數量

sentence = ''.join(words).lower()

count_of_words = {}

for i in sentence:
    if (ord(i) >= ord('a')) and (ord(i) <= ord('z')): # 要注意題目會包含「英文字母、空白、逗點、句點」，但只要輸出英文字母
        if (i not in count_of_words):
            count_of_words[i] = 1
        else:
            count_of_words[i] += 1

count_sort = sorted(count_of_words)

for i in count_sort:
    print(f'{i} : {count_of_words[i]}')