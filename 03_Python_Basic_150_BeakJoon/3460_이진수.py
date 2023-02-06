for i in range(int(input())):
    a = bin(int(input()))
    for i, v in enumerate(reversed(a)):
        if v == '1':
            print(i, end=' ')

    