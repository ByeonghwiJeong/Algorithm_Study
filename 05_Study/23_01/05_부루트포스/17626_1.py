import sys
from itertools import combinations_with_replacement
# 중복조합
input = sys.stdin.readline

MAX = 50000

def find_min_number(n):
    squares = [i*i for i in range(1, int(MAX ** (1/2))+1)]
    
    # 만약 n이 제곱수라면 - 아이디어!
    if (int(n**(1/2))) ** 2 == n:
        return 1

    # 2, 3
    for num in range(2, 4):
        # combinations_with_replacement() -> 중복조합
        combi = combinations_with_replacement(squares, num)
        sum_list = list(map(lambda x:sum(x), combi))
        # 모든 조합의 합 구하기
        if n in sum_list:
            return num

    # 1, 2, 3 아니라면 조건에 4개이하로 가능!!
    return 4

n = int(input())
print(find_min_number(n))

    