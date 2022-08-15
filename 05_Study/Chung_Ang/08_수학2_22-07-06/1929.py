# M, N = map(int, input().split())

# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, n // 2 + 1):    
#         if n % i == 0:
#             return False
#     return True

# for i in range(M, N+1):
#     if is_prime(i):
#         print(i)

'''
시간 초과 발생
'''
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

chk = [True] * (N+1)
chk[1] = False 
# 잊지말자 !!!!
for i in range(2, N+1):
    if chk[i]:
        for j in range(i*2, N+1, i):
            chk[j] = False

for i in range(M, N+1):
    if chk[i]:
        print(i)