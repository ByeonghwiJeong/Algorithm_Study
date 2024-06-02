"""
https://www.acmicpc.net/problem/2240
백준 2240. 자두나무, G2

"""
import sys

def go(idx, tree, cnt):
    if cnt < 0: return -1 # 더 이상 움직일 수 없는 경우
    if idx == N: return 0 # 끝까지 간 경우
    if dp[idx][tree][cnt] != -1: return dp[idx][tree][cnt] # 이미 계산한 경우
    ret = max(go(idx + 1, tree ^ 1, cnt - 1), go(idx + 1, tree, cnt)) 
    # 움직이지 않는 경우, 움직이는 경우
    if tree == a[idx] - 1: ret += 1 # 현재 위치에서 열매 OK : cnt + 1
    dp[idx][tree][cnt] = ret # 저장
    return ret

N, M = map(int, input().split())
a = [int(input()) for _ in range(N)]
dp = [[[-1 for _ in range(M+2)] for _ in range(2)] for _ in range(N+2)]
print(max(go(0, 1, M - 1), go(0, 0, M)))