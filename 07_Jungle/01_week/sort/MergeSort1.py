'''
합병정렬 - 주니온
<문제점>
1. 입력 리스트 S이외에 리스트 U, V 추가적으로사용
2. 메모리 비효율성
'''
def merge(U, V):
    print('Merge : ', U, V)
    S = []
    i = j = 0
    while(i < len(U) and j < len(V)):
        if(U[i] < V[j]):
            S.append(U[i])
            i += 1
        else:
            S.append(V[j])
            j += 1
    if(i < len(U)):
        S += U[i : len(U)]
    else:
        S += V[j : len(V)]
    return S

def mergesort(S):
    print('Divide : ', S)
    n = len(S)
    if(n <= 1):
        return S
    else:
        mid = n // 2
        U = mergesort(S[0 : mid])
        V = mergesort(S[mid : n])
        print("U = ",U , end=" ")
        print("V = ",V)
        return merge(U, V)
    
S = [27, 10, 12, 20, 25, 13, 15, 22]
print(mergesort(S))

"""
Divide :  [27, 10, 12, 20, 25, 13, 15, 22]
Divide :  [27, 10, 12, 20]
Divide :  [27, 10]
Divide :  [27]
Divide :  [10]
U =  [27] V =  [10]
Merge :  [27] [10]
Divide :  [12, 20]
Divide :  [12]
Divide :  [20]
U =  [12] V =  [20]
Merge :  [12] [20]
U =  [10, 27] V =  [12, 20]
Merge :  [10, 27] [12, 20]
Divide :  [25, 13, 15, 22]
Divide :  [25, 13]
Divide :  [25]
Divide :  [13]
U =  [25] V =  [13]
Merge :  [25] [13]
Divide :  [15, 22]
Divide :  [15]
Divide :  [22]
U =  [15] V =  [22]
Merge :  [15] [22]
U =  [13, 25] V =  [15, 22]
Merge :  [13, 25] [15, 22]
U =  [10, 12, 20, 27] V =  [13, 15, 22, 25]
Merge :  [10, 12, 20, 27] [13, 15, 22, 25]
[10, 12, 13, 15, 20, 22, 25, 27]
"""