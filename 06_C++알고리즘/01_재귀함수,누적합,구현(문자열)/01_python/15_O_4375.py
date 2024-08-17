'''
https://www.acmicpc.net/problem/4375
제목 : 1

문제
- 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 
- 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오

입력
3
7
9901

출력
3
6
12
'''
import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        num = 1
        count = 1

        while num % n != 0: # 1로만 이루어진 수를 만들어 n으로 나누기
            num = (num * 10 + 1) % n
            count += 1

        print(count)
    except:
        break