'''
< 파일 정리 >
문제) 
- 파일이 확장자 별로 몇 개씩 있는지
- 확장자들을 사전 순으로 정렬

'''
import sys
input = sys.stdin.readline

a = []
b = dict()
for _ in range(int(input())):
    i = input().rstrip().split('.')[1]
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
        a.append(i)
a.sort()
for j in a:
    print(j, b[j], sep=" ")

'''
입력받을 때 개행문자 지우기
'''