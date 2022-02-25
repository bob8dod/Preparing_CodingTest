# 프로그래머스 월간 코드 챌린지 P68936 쿼드압축 후 개수 세기
"""
분할정복. (재귀)
먼저 가장 큰 정사각형으로 시작해서
이를 4등분 해가면 재귀적으로 뿌리를 내려감
가장 마지막 사각형 -> 원소가 1개인 정사각형에 도달하면
그 값들을 그대로 반환
그럼 그 반환받은 재귀는 그 모든 값들이 동일한지 판단 -> 합을 통해
동일하다면 그 동일한 숫자를 반환.
동일하지 않다면 지금까지 나온 수들을 count해주고 -1을 반환.
[핵심]
문제의 역순으로 진행되는 것.
반환 값을 통해서 직관적으로 그 원소를 포함 하고 있다고 판단.
즉,
0 1 0 0 -> -1 0 -> -1
0 0 0 0    -1 1
0 1 1 1
1 1 1 1
"""


cnt0 = 0
cnt1 = 0
def div(idx, term):
    global cnt0,cnt1

    if term == 1:
        return arr[idx[0]][idx[1]]

    search = term//2
    tem0 = 0
    tem1 = 0
    for i in [idx,[idx[0],idx[1]+search],[idx[0]+search,idx[1]],[idx[0]+search,idx[1]+search]]:
        result = div(i,term//2)
        if result == 0: tem0+=1
        elif result == 1: tem1+=1


    if tem0 == 4: return 0 # 모두 0 -> 0
    elif tem1 == 4 : return 1 # 모두 1 -> 1
    else: # 다르다 -> -1
        cnt0 += tem0
        cnt1 += tem1
        return -1


def solution(_):
    global arr
    arr = _
    answer = [0,0]
    result = div([0,0],len(arr))
    if result == -1 : answer = [cnt0, cnt1]
    else:
        answer[result] = 1
    return answer
