#1342 행운의 문자열 WRONG
from itertools import permutations

S = input()
cnt = 0
print(list(permutations(S, len(S))))
for tem in permutations(S, len(S)):
    flag = True
    for i in range(len(tem)-1):
        if tem[i] == tem[i+1]:
            flag = False
            break

    if flag: cnt+=1

print(cnt)
