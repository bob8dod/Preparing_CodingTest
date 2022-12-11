# BaekJoon P6987 "월드컵" (백트래킹 | G5)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
먼저 A~F 끼리의 경기의 모든 경우의 수를 구해준 후 (경기 순서를 지정해주는 것)
depth를 통해 해당 경기의 경우의 수를 매핑
해당 경기에서 나올 수 있는 경기 결과를 백트리킹으로 전수조사.
경기 결과에 따라 각각의 승 무 패를 차감시키고
모든 경기가 끝났을 때 승 무 패 의 결과 값이 모두 0인지 판단.
아니면 일어날 수 없는 결과. 맞으면 일어날 수 있는 결과
---[비고]---
"""

from itertools import combinations

# 백트래킹
def dfs(depth):
    global cnt

    # 15번째 경기
    if depth == 15:
        cnt = 1
        for sub in res:
            if sub.count(0) != 3:
                cnt = 0
                break
        return

    # 경기 조합
    g1, g2 = games[depth]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[g1][x] > 0 and res[g2][y] > 0:
            res[g1][x] -= 1
            res[g2][y] -= 1
            dfs(depth + 1)
            res[g1][x] += 1
            res[g2][y] += 1


if __name__ == "__main__":
    answers = []
    games = list(combinations(range(6), 2))
    print(games)

    for _ in range(4):
        tmp = list(map(int, input().split()))
        res = [tmp[i:i + 3] for i in range(0, 16, 3)]
        cnt = 0
        dfs(0)
        answers.append(cnt)

    print(*answers)
