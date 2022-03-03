# 프로그래머스 2019 카카오 개발자 겨울 인턴십 P64064 불량사용자
"""
가장 먼저 각 banned_id에 해당하는 모든 user를 기록해주고 (result)
그 기록된 result에서 뽑을 수 있는 모든 경우의 수를 구함
이때, 중복을 고려해야되기에 result에서 중복을 제거하고 난 후의 길이가 원하는 길이와 일치하는 지 확인한 후
각 user를 하나의 문자열로 만들어주며 결과 내에서도 중복이 일어나는지 판단
"""
from itertools import product

def solution(user_id, banned_id):

    result = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for user in user_id:
            if len(user) != len(banned_id[i]) : continue
            flag = 1
            for u,b in zip(user,banned_id[i]):
                if b == '*': continue
                if u != b:
                    flag=0
                    break

            if flag == 1 :
                result[i].append(user)
    answer = set()
    for i in product(*result):
        if len(set(i)) == len(banned_id):
            answer.add(''.join(sorted(i)))

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))


