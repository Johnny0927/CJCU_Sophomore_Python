sub = input()
main = input()

times = 0
sub_len = len(sub)
for i in range(len(main)):
    if (main[i:(i + sub_len)] == sub):
        times += 1

print(times)