S = input().rstrip()
_set = set()
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        _set.add(S[i:j])
print(len(_set))
