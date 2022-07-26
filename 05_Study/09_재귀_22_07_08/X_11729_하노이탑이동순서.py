'''
3개의 장대가 있다.
반경이 서로 다른 N개의 원판이 쌍여 있다.
각 원판은 반경이 큰 순서대로 쌓여 있다.

1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
2. 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야한다.

첫번째 줄에 옮긴 횟수 K를 출력
두번째 줄부터 수행 과정을 출력한다.
start, end는 1 2 3중 가능 
6 - start - end  ;  
    - 1 2 3 합이 6이므로 2가지(start, end)위치를 제외한 하나의 값

점화식 A(n, start, end) : n개를 start >> end로 옮기는 수
 - 1 ; A(n-1, start, 6 - end - start) : n-1개를 옮기는 수 (2번으로 이동)
 - 2 ; 1 : 맨 마지막 판을 3번으로 이동
 - 3 ; A(n-1, start) : n-1개를 옮기는 수 (2번으로 이동)
 
 >>> 갯수 : A(n) = 2 * A(n - 1) +  1
 >>> 초기값 : A(1) = 1 
 A(n) = 2^n + b >>> 2^n - 1

'''
def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi_tower(n - 1, start, 6 - end - start)
    print(start, end)
    hanoi_tower(n - 1, 6 - end - start, end)

n = int(input())
print(2**n - 1)
hanoi_tower(n, 1, 3)