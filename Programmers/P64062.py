# 프로그래머스 2019 카카오 개발자 겨울 인턴십 P64062 징검다리 건너기
"""
이진탐색의 응용 버전
넘어갈 수 있는 인원을 탐색할 배열이라고 생각. -> 1 ~ 20000000
여기서 가능한 최대의 인원을 이진 탐색하는 것.
mid를 구해서 모든 돌멩이들의 수를 빼주고
뺀 후에 그 연속된 0의 개수가 K가 안된다면 -> 현재 그 mid 보다 더 많은 인원이 지나갈 수 있다는 것
뺀 후에 그 연속된 0의 개수가 K가 된다면 -> 현재 그 mid 이거나 더 적은 인원으로 지나가야 된다는 것
"""

def solution(stones, k):
    left = 1
    right = 200000000
    while left < right:
        temp = stones.copy()
        mid = (left+right) // 2
        # print(left, mid, right)
        cnt = 0
        flag = False
        for t in temp:
            re = t - mid
            if re <= 0: cnt += 1
            else: cnt = 0

            if cnt == k:
                flag = True
                break

        if flag:
            right = mid
        else:
            left = mid + 1

    return left
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
