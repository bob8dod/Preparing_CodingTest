# 백준 P1932 DP 정수 삼각형
"""
맨 처음엔 BFS로 모든 노드를 탐색하며
그 노드까지의 합산을 dp를 통해 계산하여 저장함
-> 메모리 초과.
즉, Q를 사용하고 gmap과 크기가 동일한 dp를 추가적으로 사용하면서 메모리가 초과됨
-> 결국, 입력을 받으면서 동시에 판단하여 바로 DP를 생성하여, gmap과 Q를 사용하지 말아야했음
[풀이]
입력을 받음과 동시에 판단.
현재 search하는 노드의 윗노드 중 닿을 수 있는 노드의 크기들을 비교하여
그 즉시 해당 노드의 DP에 저장.
"""
import sys

def main():
    global N, gmap
    N = int(sys.stdin.readline())
    dp = [list(map(int,sys.stdin.readline().split()))]
    for i in range(1,N):
        dp.append(list(map(int,sys.stdin.readline().split())))
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif j == len(dp[i])-1:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
            else:
                bigger = max(dp[i-1][j-1], dp[i-1][j])
                dp[i][j] = bigger + dp[i][j]

    print(max(dp[-1]))

if __name__ == "__main__":
    main()
