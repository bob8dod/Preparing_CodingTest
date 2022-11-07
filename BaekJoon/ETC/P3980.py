# BaekJoon P3980 "선발 명단" (백트래킹 | G5)
"""
---[실수]---
1. permuations 로 해결하려 함 -> 겁나 오래 걸림
2. 인덱스가 0부터 시작한다는 것을 인지하지 못한 채, 끊어주는 부분을 12로 설정 (if position == 12)
    - 주의 : defaultdict 로 설정했기에 position_players[12] 는 key error 가 나지 않았음 => position_player 에 {12:[]} 가 그냥 생겨버리기에.
---[부족한 점]---
- 백트래킹을 combinations 로 해결해왔어서 직접 내가 실제 백트래킹을 구현하는 과정에 있어서 부족함을 느낌
---[풀이]---
먼저 position 별 가능한 player 를 dictionary 로 정리해준 후 (정리 안해도 됨 -> 더 이해하기 쉽고 편리하게 접근하고자 생성함)
dfs(ncr)을 통해서 현재 focus 된 position 에 가능한 player 를 배치해 주면서 모든 포지션의 배치가 완료될 때 까지 나아가는 것
이때 중요한 부분은 dfs 전에 해당 player 를 배치하지 않도록 visited 처리 해준 후
dfs 가 끝난 후 visited 를 해제해주면서 다른 다른 뿌리에서는 이전 뿌리에 대한 영향을 없개 해주는 것
또한, global 을 사용하지 않게 하기 위해 dfs 의 반환값을 지정했으며,
이에 따라 dfs 는 현재 뿌리로 내려오는 모든 선수들의 능력치 합과, 지금까지 search 된 포지션의 최대 능력치 정보를 가지고 있어야 함 -> total, max_total
max_total 은 dfs 가 끝나면 새로 업데이트하여 다음 뿌리로 넘어가, 현재까지의 최대 능력치를 고려해주어야 함 -> max_total = dfs(...)
---[비고]---
https://www.acmicpc.net/board/view/36219
- 백트래킹의 최대값 반영을 끊어주는 부분이 아닌, 중간에 적용할 경우 오류 발생.
- 위의 링크의 반례를 통해서 아래 코드는 옳지 않다는 것을 알 수 있음
=> 결론 : 백트래킹의 최대값 반영은 마지막에 끊어주는 부분에서 이루어져야함!
def dfs(position, position_players, batched_player):

    if position == 11: # 실수 -> 12로 잡음
        return 0

    best_capacity = 0
    for player, capacity in position_players[position]:
        if batched_player[player]: continue
        batched_player[player] = 1
        best_capacity = max(best_capacity, capacity + dfs(position + 1, position_players, batched_player))
        batched_player[player] = 0

    return best_capacity

개인적으로 굉장히 좋은 문제였다고 생각함. -> 백트래킹을 직접 구현해보는 문제였기에.
또한, 한번 쯤은 global 을 사용하지 않고 dfs 의 반환값을 이용하여 구현해 보는 것을 추천 -> 재귀에 대해서 깊은 이해가 가능해짐
"""
import sys
from collections import defaultdict
from itertools import permutations # 첫 시도 -> 줠라 오래 걸림

def make_position_dict(infos):
    position_players = defaultdict(list)
    for position in range(11):
        for player_num in range(11):
            capacity = infos[player_num][position]
            if capacity:
                position_players[position].append([player_num, capacity])
    return position_players


def dfs(position, position_players, batched_player, total, max_total):

    if position == 11: # 실수 -> 12로 잡음
        max_total = max(max_total, total)
        return max_total
        # 백 트래킹의 핵심 -> 조건에 해당될 때 최대값을 반영해야 함.

    for player, capacity in position_players[position]:
        if batched_player[player]: continue
        batched_player[player] = 1
        max_total = dfs(position + 1, position_players, batched_player, total+capacity, max_total)
        batched_player[player] = 0

    return max_total

def solution(infos):
    position_players = make_position_dict(infos)
    batched_player = [0 for _ in range(11)]
    answer = dfs(0, position_players, batched_player, 0, 0)
    return answer

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(11)]
        print(solution(inputs))
