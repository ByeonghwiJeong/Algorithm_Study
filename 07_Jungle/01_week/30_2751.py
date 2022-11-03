import sys
input = sys.stdin.readline

print(*sorted([int(input()) for _ in range(int(input()))]), sep='\n')