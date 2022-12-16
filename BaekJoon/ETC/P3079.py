import sys
input = sys.stdin.readline


def check(mid, buses):
    total = 0
    for buse in buses: # 주어진 시간에 각 심사대는 최대 몇명을 처리할 수 있는가
        total += mid // buse # 를 누적해서 계산해주면 -> 주어진 시간에 처리할 수 있는 최대 인원
    return total

def solution(n, m, buses):
    left = 1
    right = 10**9 * m
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid, buses) >= m:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    inputs = [int(input().strip()) for _ in range(N)]
    print(solution(N, M, inputs))
