# 백준 BFS/DFS,백트래킹 P16953 A->B
"""
처음에는 DP로 풀었지만, 입력 범위 자체가 10^9 이였기에
애초에 메모리초과, 시간초과에 걸릴 수 밖에 없음.
결국 그래프이론과 백트래킹을 사용해서 풀어야 함!
[풀이]
도달해야 되는 지점 end에서 백트래킹으로
start까지 가게끔 설정.
그 때 현재 숫자가 2로 나누어지거나 1로 끝나게 되면
그 지점에서 계속 백트래킹 진행
결론적으로 start에 도달하면 cnt를 반환하고
start를 넘어가는 순간 or start에 도달하지 못하는 순간에는 -1 을 반환
"""
import sys
from collections import deque

def sub(): # DP로 풀었던 과정 (틀림)
    s, e = map(int, input().split())
    dp = [0 for _ in range(e+1)]
    for i in range(s):
        dp[i] = sys.maxsize
    dp[s] = 1
    for i in range(s+1,e+1):
        mul = sys.maxsize
        plus = sys.maxsize
        if i%2 == 0: mul = dp[i//2] + 1
        if i%10 == 1: plus = dp[i//10] + 1
        dp[i] = min(mul, plus)

    print(dp[-1] if dp[-1]!=sys.maxsize else -1)

def bfs(s,e):
    Q = deque([[e,1]])
    while Q:
        curr, cnt = Q.popleft()
        print(curr)
        if curr==s: return cnt
        if curr < s: return -1 # start보다 작은 지점으로 넘어가면
        if curr%2 == 0:
            Q.append([curr//2,cnt+1])
        elif curr%10 == 1:
            Q.append([curr//10,cnt+1])

    return -1 # start보다 큰 지점에서 끝나는 경우



def main():
    s, e = map(int, input().split())
    print(bfs(s,e))

if __name__ == '__main__':
    main()
