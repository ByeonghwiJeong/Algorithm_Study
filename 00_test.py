x = [[0, 1, 1, 0],[0, 1, 1, 0],[0, 1, 0, 0],[0, 1, 0, 0]]
print(x[2:0])
tmp1 = [y[2:] for y in x[2:]]
print(tmp1)
tmp2 = [[0] * 2 for _ in range(2)]
print(tmp2)

print('0000000')
if tmp1 == tmp2:
    print('같다')
else:
    print('다르다')