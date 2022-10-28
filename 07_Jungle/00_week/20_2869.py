'''
높이 v 나무
낮 a미터 up
밤 b미터 down
몇일걸리는지
'''
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
q = (v-b) / (a - b)
if int(q) == q:
    print(int(q))
else:
    print(int(q) + 1)