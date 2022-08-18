'''
하노이 탑

f(n)
        <1>     <2>     <3>
              f(n-1)        : 2번으로 옮기는 경우
                        1   : 제일큰판 아래로 옮기는경우
                        f(n-1)
f(n) = 1 + 2 * f(n-1)
f(1) = 1
f(n) = 2^n - 1 

6 - start - end  ;  
    - 1 2 3 합이 6이므로 2가지(start, end)위치를 제외한 하나의 값

점화식 A(n, start, end) : n개를 start >> end로 옮기는 수
 - 1 ; A(n-1, start, 6 - end - start) : n-1개를 옮기는 수
     (예 : n-1를 1번 >> 2번)
 - 2 ; 1 : 맨 마지막 판을 3번으로 이동
     (예 : 1을 1번 >> 3번)
 - 3 ; A(n-1, 6 - end - start, end) : n-1개를 옮기는 수 
     (예 : n-1를 2번 >> 3번)
'''
import sys
input = sys.stdin.readline

N = int(input())

def hanoi(n, st, en):
    if n == 1:
        print(st, en)
        return
    hanoi(n - 1, st, 6 - st - en)
    print(st, en)
    hanoi(n - 1, 6 - st - en, en)

print(2**N - 1)
print(hanoi(N, 1, 3))
    

