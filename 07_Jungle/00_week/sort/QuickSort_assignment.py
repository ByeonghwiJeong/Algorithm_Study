def partition(a, low, high):
    n = high + 1
    pl = low      # 왼쪽커서
    pr = high  # 오른쪽커서
    print('피벗 인덱스 : ', (low + high + 1) // 2)
    x = a[(low + high + 1) // 2] # 피벗(가운데원소)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    # print(f'피벗: {x}')
    # print(f'<피벗이하의 그룹>')
    # print(*a[0:pl]) 

    if pl > pr + 1:
        # print('<피펏과 일치하는 그룹>')
        # print(*a[pr+1:pl])
        return pr, pl-1

    # print(f'<피펏 이상인그룹>')
    # print(*a[pr+1:n])
    return pr, pr


x = [5, 8, 4, 2, 6, 1, 3, 9, 7]
print("첫번째 Before : ", x)
pv1, pv2 = partition(x, 0, len(x) - 1)
print("첫번째 After: ", x)
print("두번째 Before: ", x[0:pv1+1])
partition(x, 0, pv1)
print("두번째 After: ", x[0:pv1+1])
print("세번째 Before: ", x[pv2+1:])
partition(x, pv2, len(x) - 1)
print("세번째 A: ", x[pv2+1:])
