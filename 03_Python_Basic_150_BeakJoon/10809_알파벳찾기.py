alpha = 'abcdefghijklmnopqrstuvwxyz'
l = [-1] * 26
check = []
ss = input()
for i in range(len(ss)):
    if ss[i] in check:
        continue
    a = alpha.index(ss[i])
    l[a] = i
    check.append(ss[i])
l = list(map(str, l))
print(' '.join(list(map(str, l))))
    