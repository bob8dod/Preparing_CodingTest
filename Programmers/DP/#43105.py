# 43105 정수삼각형_40min
"""
DP사용
가장 먼저 주어진 triangle로 tri_map을 만듦
tri_map은 해당 triangle에 맞게 행렬로 만든 것.
예를 들면
. . 7 . .
. 3 . 8 .
8 . 1 . 0 
이런 식으로 tri_map을 만들고 그에 따른 계산 결과인 dp도 빈 상태로 생성해줌
그 후 하나 하나 확인하면서 (BFS방식으로) 내려감
이 때 현재 계산한 덧셈값이 이전에 계산했던 값보다 크면 해당 값 교체
마지막 층의 계산 결과 중 max 값 반환
"""
def clac(tri_map):
    global dp
    dp = [[0 for _ in range(m_size)] for _ in range(n)]
    dp[0][m_size // 2] = tri_map[0][m_size // 2]
    for i in range(n-1):
        for j in range(m_size):
            if tri_map[i][j] != -1:
                left, right = j-1, j+1
                now_l = dp[i][j] + tri_map[i+1][left]
                now_r = dp[i][j] + tri_map[i + 1][right]
                if dp[i+1][left] < now_l:
                    dp[i+1][left] = now_l
                if dp[i + 1][right] < now_r:
                    dp[i + 1][right] = now_r

def solution(triangle):
    global n, m_size, mid
    n = len(triangle)
    m_size = n*2-1
    mid = m_size // 2
    tri_map = [[-1 for _ in range(m_size)] for _ in range(n)]
    for i in range(n):
        k = mid
        for j in range(len(triangle[i])):
            tri_map[i][k] = triangle[i][j]
            k+=2
        mid-=1
    clac(tri_map)
    return max(dp[-1])
