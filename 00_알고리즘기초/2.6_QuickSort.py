def partition(S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        if(S[i] < pivotitem):
            j += 1
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint

def quicksort(S, low, high):
    if (high > low):
        pivotpoint = partition(S, low, high)
        quicksort(S, low, pivotpoint - 1)
        quicksort(S, pivotpoint + 1, high)

# S = [15, 22, 13, 27, 12, 10, 20, 25]
# print('Before:', S)
# quicksort(S, 0, len(S) - 1)
# print(' After:', S)

# S = [15, 22, 13, 27, 12, 10, 20, 25]
# print('Before:', S)
# partition(S, 0, len(S) - 1)
# print(' After:', S)