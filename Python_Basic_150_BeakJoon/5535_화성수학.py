for _ in range(int(input())):
    test = list(input().split())
    for i in range(len(test)):
        if i == 0:
            ans = float(test[i])
        else:
            if test[i] == '@':
                ans *= 3
            elif test[i] == '%':
                ans += 5
            elif test[i] == '#':
                ans -= 7
    print(f'{ans:.2f}')
