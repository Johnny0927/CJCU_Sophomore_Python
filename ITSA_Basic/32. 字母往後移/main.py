sentence = input()
jump = int(input())
new_sentence = ''
for s in sentence:
    s = ord(s)
    if (ord('A') <= s <= ord('Z')):
        if ((s + jump) > ord('Z')):
            s = ((s + jump) - ord('Z') + ord('A') - 1)
        else:
            s = (s + jump)

    elif (ord('a') <= s <= ord('z')):
        if ((s + jump) > ord('z')):
            s = ((s + jump) - ord('z') + ord('a') - 1)
        else:
            s = (s + jump)

    elif (ord('0') <= s <= ord('9')):
        if ((s + jump) > ord('9')):
            s = ((s + jump) - ord('9') + ord('0') - 1)
        else:
            s = (s + jump)
    
    new_sentence += chr(s)

print(new_sentence)