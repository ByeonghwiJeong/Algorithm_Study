'''
https://www.acmicpc.net/problem/1629
제목 : 곱셈

문제
- 자연수 A를 B번 곱한 수를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
- A, B, C는 모두 2,147,483,647


'''
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def recur(n, x): # n을 x번 곱하기
    if x == 1: return a % c
    r = recur(n, x // 2)
    if x % 2: return r ** 2 * n % c
    else: return r ** 2 % c

print(recur(a, b))