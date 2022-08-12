'''

입력)
    - 1 : 나무의 수 N, 가지고 가려는 나무의 길이 M
    N~[1, 1,000,000] M~[1, 2,000,000,000]
    - 2 : 나무의 높이


'''

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

def cal_length(x):
    sum = 0
    for t in trees:
        if t > x:
            sum += t - x
    return sum

def binary_search(st, en, target):
    if st > en:
        return en

    mid = (st + en) // 2
    sum = cal_length(mid)

    if sum == target:
        return mid
    elif sum < target: # 아래로 가야 sum이 커진다
        return binary_search(st, mid - 1, target)
    else:
        return binary_search(mid + 1, en, target)

print(binary_search(1, max(trees), M))