'''
한수는 x, y에 있다.
직사각형은 각변이 평행하고
왼쪽 아래 꼭짓점은 (0, 0)
오른쪽 꼭짓점은 (w, h)
입력) 
    - x, y, w, h
'''
import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))
