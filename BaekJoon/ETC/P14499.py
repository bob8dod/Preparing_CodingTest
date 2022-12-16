import sys

input = sys.stdin.readline


def change_dice(dice, order):
    e, w, s, n, t, b = dice
    if order == 1:
        dice[0], dice[1], dice[4], dice[5] = b, t, e, w
    elif order == 2:
        dice[0], dice[1], dice[4], dice[5] = t, b, w, e
    elif order == 3:
        dice[2], dice[3], dice[4], dice[5] = t, b, n, s
    elif order == 4:
        dice[2], dice[3], dice[4], dice[5] = b, t, s, n


def solution(n, m, x, y, k, graph, orders):
    answer = []

    d = ((0, 1), (0, -1), (-1, 0), (1, 0))
    dice = [0 for _ in range(6)]
    ci, cj = x, y
    for order in orders:
        di, dj = d[order - 1]
        ni, nj = ci + di, cj + dj
        if 0 <= ni < n and 0 <= nj < m:
            change_dice(dice, order)
            if graph[ni][nj] == 0:
                graph[ni][nj] = dice[5]  # bottom
            else:
                dice[5] = graph[ni][nj]
                graph[ni][nj] = 0

            ci, cj = ni, nj
            answer.append(dice[4])

    return answer


if __name__ == '__main__':
    N, M, X, Y, K = map(int, input().split())
    inputs1 = [[*map(int, input().split())] for _ in range(N)]
    inputs2 = [*map(int, input().split())]
    print(*solution(N, M, X, Y, K, inputs1, inputs2), sep="\n")
