# 프로그래머스 월간 코드 챌린지 시즌3 P87390 n^2 배열 자르기
def solution(n, left, right):

    left_idx = [left//n, left%n]
    right_idx = [right//n, right%n]
    result = []
    flag = 0
    for i in range(left_idx[0], right_idx[0]+1):
        for j in range(n):
            if [i,j] == left_idx: flag = 1
            if flag == 1: result.append(max(i,j)+1)
            if [i,j] == right_idx:
                return result
