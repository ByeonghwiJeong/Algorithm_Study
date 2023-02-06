def binary_search(array, st, en, target):
    if st > en:
        return en
    mid = (st + en) // 2
    hight_sum = 0

    for i in array:
        if i < mid:
            continue
        else:
            hight_sum += i - mid

    if hight_sum == target:
        return mid
    elif hight_sum < target:
        return binary_search(array, st, mid -1, target)
    else:
        return binary_search(array, mid + 1, en, target)

N, M = map(int, input().split())
array = list(map(int, input().split()))
result_index = binary_search(array, 0, max(array) - 1, M)
print(result_index)
