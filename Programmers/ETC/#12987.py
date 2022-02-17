# 12987 숫자게임 _ 30m
"""
주어진 순서는 사실 상관없다고 판단,
두 배열을 모두 정렬하여, 작은 놈들부터 비교할 수 있도록 설정.
[개념]
지금 처리해야될 남은 놈들로부터 점수를 얻을 수 있는 놈이 하나도 없다면 (작거나 같은 경우),
차피 어떤 놈들한테도 지기 때문에 현재 카드를 버리는 카드로써 가장 큰놈과 상대하게 하는 전략.
[풀이]
만약 b가 a 보다 작거나 같은 경우, 아무것도 하지 않고 넘어감. -> 버리는 카드, 개념상으로는 가장 큰놈과 상대하게 하는 것
b가 a보다 크다면 거기서 그냥 그놈을 마크함. 차피 뒤의 b들은 현재의 a를 모두 처리할 수 있기 때문에
현재 처리해야될 애들 중 가장 작은 b를 현재 상대할 애들 중 가장 작은 a를 마크하게 하면 됨.
"""
def solution(A, B):
    answer=0
    A.sort()
    B.sort()

    i = 0

    for b in B:
        if A[i] < b :
            answer+= 1
            i += 1

    return answer
