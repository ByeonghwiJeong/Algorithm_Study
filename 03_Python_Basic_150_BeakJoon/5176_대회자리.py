for _ in range(int(input())):
    P, M = map(int, input().split())
    # P : 참가자의 수
    # M : 자리의 수
    # 참가자수 
    l = []
    for _ in range(P):
        l.append(int(input()))
    print(P - len(set(l)))