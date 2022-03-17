# 백준 DP P11052 카드 구매하기
"""
전형적인 DP문제.
내가 살 수 있는 개수를 기준으로 DP를 진행하고
이 DP를 P의 원소들을 추가하며 해당 원소까지 고려했을 때의 최적DP를 구하는 방식으로 진행
여기서 중요한 점은 각 원소가 현재 DP에 영향을 미칠 수 있는 조건을 고려해야됨.
1. 현재 p만으로 dp를 구성할 수 있나 -> di%pi==0
2. 그게 아닌가 (p로만 구성할 수 없고 다른 p와 같이 구성해야됨) -> else
=> 결론적으로 이전 p들로 구성한 dp값과 1과 2의 값들을 비교해서 가장 큰값을 dp에 저장
"""
import sys

def main():
    N = int(sys.stdin.readline().strip())
    P = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(N+1)]
    for pi in range(1,N+1):
        for di in range(pi,N+1):
            first, second = 0,0
            if di%pi==0: first = P[pi]*(di//pi)
            # if di!=pi: second = P[pi] + dp[di-pi]
            else: second = P[pi] + dp[di-pi]
            dp[di] = max(dp[di],first,second)

    print(dp[-1])



if __name__ == '__main__':
    main()
