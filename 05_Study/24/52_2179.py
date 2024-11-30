# str = input().upper()
# dic = dict()
# for s in str:
#     if s in dic:
#         dic[s] += 1
#     else:
#         dic[s] = 1
# cnt = 0
# max_v = max(dic.values())
# for k, v in dic.items():
#     if v == max_v:
#         ans = k
#         if cnt == 1:
#             print('?')
#             break
#         cnt += 1
# else:
#     print(ans)

from collections import Counter

word = input().strip().upper()
freq = Counter(word)
max_freq = max(freq.values())
most_common = [char for char, count in freq.items() if count == max_freq]
print(most_common[0] if len(most_common) == 1 else '?')