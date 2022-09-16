words = input().lower().split()

check = []

result = []
for w in words:
    if (w not in check):
        result.append(w)
        check.append(w)

print(' '.join(result))


# 本題使用 set 型態做輸出，雖然可以滿足所有字只出現一次的需求，但順序會錯亂導致送出後答案錯誤