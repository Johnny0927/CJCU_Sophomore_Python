while True:
    word = input()
    
    word_reverse = word[::-1]

    if (word == word_reverse):
        print('YES')
    else:
        print('NO')