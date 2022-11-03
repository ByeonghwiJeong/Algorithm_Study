def partition(a):
    n = len(a)
    pl = 0      # 왼쪽커서
    pr = n - 1  # 오른쪽커서
    x = a[n // 2] # 피벗(가운데원소)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'피벗: {x}')
    print(f'<피벗이하의 그룹>')
    print(*a[0:pl]) 

    if pl > pr + 1:
        print('<피펏과 일치하는 그룹>')
        print(*a[pr+1:pl])

    print(f'<피펏 이상인그룹>')
    print(*a[pr+1:n])



x = [5, 8, 4, 2, 6, 1, 3, 9, 7]
partition(x)