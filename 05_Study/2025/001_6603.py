'''
https://www.acmicpc.net/problem/6603
제목 : 로또

문제)
- {1, 2, ..., 49}에서 수 6개를 고른다
- 49가지 수 중 k(k>6)개의 수를 골라 집합 S
- 그 수만 가지고 번호를 선택
- k=8, S={1,2,3,5,8,13,21,34}
- [1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34]

입력)
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

출력)
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
'''
import sys
input = sys.stdin.readline


def dfs(result, idx, depth): 
    if depth == 6:
        print(*result)
        return
    for i in range(idx, K):
        result[depth] = S[i]
        dfs(result, i+1, depth+1)


if __name__ == '__main__':
    while True:
        K, *S = list(map(int, input().split()))
        if K == 0:
            break
        result = [0] * 6
        dfs(result, 0, 0)

        # from itertools import combinations
        # for comb in combinations(S, 6):
        #     print(*comb)

        print()









    



        



