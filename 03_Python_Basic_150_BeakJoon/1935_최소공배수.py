'''
너무한 실수다 !!!!!!!!!
절대로 잊지말자
재귀방식으로 구현시
내부 함수 호출에서 return 필수!
'''
def gcd(a,b):
    c = a % b
    if c == 0:
        return b
    return gcd(b, c)

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(A*B//gcd(A,B))