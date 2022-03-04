# 백준 BruteForce P2468 안전 영역
"""
주어진 입력 범위를 보고 Greedy로 굳이 풀지 않고
그냥 BruteForce로도 통과할 수 있겠다 생각하여 BF로 진행
0~100 까지 모든 경우에 대해 dfs를 진행하여 몇개의 안전지대가 있는지 확인
여기서 cnt의 기준을 잘못 잡고 풀어 10분 정도 날아감 -> 주의
"""
import copy
import sys
sys.setrecursionlimit(1000000)

di = [0,1,0,-1]
dj = [1,0,-1,0]

def dfs(tmap,visited,i,j):
    visited[i][j] = 1

    for ti,tj in zip(di,dj):
        ni = i+ti
        nj = j+tj
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and tmap[ni][nj] > 0:
            dfs(tmap,visited,ni,nj)

def main():
    global N
    N = int(input())
    gmap = [list(map(int,input().split())) for _ in range(N)]

    max_cnt = 0
    for depth in range(0,101):
        tmap = copy.deepcopy(gmap)
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                tmap[i][j] -= depth

        cnt = 0
        for i in range(N):
            for j in range(N):
                if tmap[i][j] > 0 and not visited[i][j]:
                    cnt+=1
                    dfs(tmap,visited,i, j)

        max_cnt = max(max_cnt, cnt)

    print(max_cnt)


if __name__ == "__main__":
    main()

