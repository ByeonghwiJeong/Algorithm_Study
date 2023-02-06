str = input().upper()
dic = dict()
for s in str:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
cnt = 0
max_v = max(dic.values())
for k, v in dic.items():
    if v == max_v:
        ans = k
        if cnt == 1:
            print('?')
            break
        cnt += 1
else:
    print(ans)
        
