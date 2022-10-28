'''
< 하노이탑 > 
- 한번에 다른 한개의 원판만 이동
- 쌓아 높은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

입력)
- 첫번째 장대의 원판의 개수
출력)
- 오
'''
def hanoi(a, b, n):
    if n == 1:
        print(a, b)
        return
    else:
        hanoi(a, 6-a-b, n-1)
        print(a, b)
        hanoi(6-a-b, b, n-1)
        return 
N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi(1, 3, N)