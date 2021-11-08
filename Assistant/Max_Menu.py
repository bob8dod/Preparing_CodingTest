n = int(input())
s=[]
for i in range(n):
    p = input()
    s.append(p)

max_menu = s[0]
max_cnt = 0
for i in range(n):
    cnt = 1
    if s[i] not in s[:i]:
        for j in range(i+1,n):
            if s[i] == s[j]:
                cnt += 1
    if max_cnt < cnt:
        max_menu = s[i]
        max_cnt = cnt

print('%s : %d' %(max_menu,max_cnt))
