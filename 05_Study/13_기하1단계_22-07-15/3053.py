'''
택시 기하학에서 두 점
T1(x1, y1) T2(x2, y2)
D(T1, T2) = |x1 - x2| + |y1 - y2|
택시 기하학에서 원의 정의는 유클리드 기하학에서 원의 정의와 같다.
원 : 평면 상의 어떤점에서 거리가 일정한 점들의 집합
반지름 R이 주어졌을 
'''
from math import pi
import sys
input = sys.stdin.readline

R = int(input())
print(round(pi * R**2, 6))
print(R**2 * 2)
