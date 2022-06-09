# BaekJoon P14503 로봇 청소 ( 구현, DFS | Gold5)
"""
[실수]
dfs의 반환값 주의필요.
처음 solution에서 return 1+ 필수.
 -> 처음 위치에서 청소를 시작하므로.

[부족한 점]
구현하면서 흐름을 놓치는 경우가 있음.
dfs의 return값 설정 부분이 좀 더 명확할 필요가 있음

[풀이]
주어진 위치와 방향을 기점으로 dfs 시작.
일단 dfs 들어왔다는 것은 현재 위치에 대한 청소를 무조건 한다고 설정
그 다음 문제 조건에 맞게 구현
이동하지 않고 4번 회전할 경우에 대한 처리가 필요하므로
회전 횟수인 i와 회전을 하는 While문으로 처리
일단 무조건 왼쪽으로 회전해야되므로 왼쪽으로 회전,
그 후 2-a 조건에 맞는 지 판단 -> 맞으면 dfs 뿌리 내리기 (청소)
이때 (1+)는 다음 dfs의 청소 횟수를 의미. (재귀함수의 return 특징 활용)
추가로 2-b 조건 설정
즉, 그냥 왼쪽으로 회전 후
    a. 이동하여 청소(추가 dfs)
    b. 4번 회전의 경우
이렇게 진행
"""

# 빈 칸 : 0, 벽 : 1, 청소 : 2

di=[[-1,0],[0,1],[1,0],[0,-1]]

def dfs(r,c,d,gmap):
    gmap[r][c] = 2 # 현재 위치 청소 (1번 조건)
    i = 1
    while True:

        d = d-1 if d != 0 else 3 # 왼쪽으로 회전
        li, lj = di[d]

        if gmap[r+li][c+lj] == 0: # (2-a 번 조건)
            return 1 + dfs(r+li,c+lj,d,gmap)

        if i == 4: # (2-b 번 조건)
            back = (d+2)%4
            bi, bj = di[back]
            if gmap[r+bi][c+bj] == 1:
                return 0
            else:
                r,c = r+bi,c+bj
                i = 0

        i+=1


def solution(n,m,r,c,d,gmap):
    return 1 + dfs(r,c,d,gmap)


if __name__ == '__main__':
    n,m = map(int,input().split())
    r,c,d = map(int,input().split())
    gmap = [list(map(int,input().split())) for _ in range(n)]

    print(solution(n,m,r,c,d,gmap))
