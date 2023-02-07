'''
< 피자판매 >
https://www.acmicpc.net/problem/2632
문제)
- 두 종류 피자 A, B
- 각 종류의 피자는 다양한 크기의 여러 개의 피자 조각으로 구성
- 각 조각에 쓰여진 숫자는 피자조각의 크기를 나타냄
- 한종류의 피자를 2조각 이상 판매할 때는 연속된 조각들을 잘라서 판매
- 이때 판매한 피자조각의 크기 합이 주문한 크기가 되어야 한다.
입력)
- 1     : 손님이 구매하고자 하는 피자크기 2,000,000 이하 자연수
- 2     : A, B 피자조각의 개수 m, n
- 3[m]  : 미리잘린 A피자 크기
- 4[m]  : 미리잘린 B피자 크기
출력)
- 1     : 피자를 판매하는 방법의 가지 수를 나타내는 정수\
    없는경우 숫자 0 출력
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

X = int(input())
n, m = map(int, input().split())

def go(x, psum, _dict):
    for i in range(1, x + 1): # interval
        # for j in range(i, x + i):
        #     tmp = psum[j] - psum[j - i]
        for j in range(x):
            tmp = psum[j + i] - psum[j]
            _dict[tmp] += 1
            if i == x: break
    return


A = [0]
B = [0]
psum_A = [0]
psum_B = [0]
for i in range(1, n + 1):
    tmp = int(input())
    A.append(tmp)
    psum_A.append(psum_A[i - 1] + A[i])
for i in range(n + 1, 2*n + 1):
    psum_A.append(psum_A[i - 1] + A[i - n])
for i in range(1, m + 1):
    tmp = int(input())
    B.append(tmp)
    psum_B.append(psum_B[i - 1] + B[i])
for i in range(m + 1, 2*m + 1):
    psum_B.append(psum_B[i - 1] + B[i - m])

dict_A = defaultdict(int)
dict_B = defaultdict(int)

# dict_A = defaultdict(int)
# dict_B = defaultdict(int)

go(n, psum_A, dict_A)
go(m, psum_B, dict_B)

ret = 0
for i in range(1, X):
    ret += dict_A[X - i] * dict_B[i]
ret += dict_A[X]
ret += dict_B[X]
print(ret)
'''
원형 고리 구조!!! (시작과 끝이 이어짐)
    - 선형적인 자료구조를 두개 이어붙이자!
    - 누적합도 원형구조를 고려해서 계산
<풀이법>
1. A, B 각각의 조각에 있어서 누적합배열 psum_A, psum_B을 정의
    - 초기값 [0]
2. 누적합 배열에 원소를 넣을때 for문 2회씩 : Index기준
    1) 1 ~ n, 1 ~ m 
    2) n+1 ~ 2*n, m+1 ~ 2*m 
3. 해쉬맵(dict or map)을 선언 - 파이썬 defaultdict
4. 전구간에서 interval을 기준으로 전구간을 체크해서 dict update 
    key : 합
    value : 수
5. 원하는 수 X를 기준으로 결과에
    1) + dict_A[X]
    2) + dict_B[X]
    3) 전구간 for문  += dict_A[X - i] * dict_B[i]

'''