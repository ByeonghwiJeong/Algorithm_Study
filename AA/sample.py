def solution(nums):
    from itertools import combinations
    answer = 0
    for a in combinations(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j == 0:
                break
        else:
            answer += 1
    return answer