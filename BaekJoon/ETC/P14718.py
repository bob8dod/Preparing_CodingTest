# BaekJoon P14718 "빗물" (구현, 시뮬레이션 | G5)
import sys


def cal(part, start):
    waters = 0
    for w in part:
        waters += (start - w)

    return waters

def last(end, walls):
    walls.reverse()
    walls.append(end)
    answer = 0
    start = walls[0]
    part = []
    for idx, w in enumerate(walls):
        if w < start:
            part.append(w)
        else:
            answer += cal(part, start)
            part = []
            start = w

    return answer

def solution(w, h, walls):
    answer = 0
    start = walls[0]
    part = []
    for idx, w in enumerate(walls):
        if w < start:
            part.append(w)
        else:
            answer += cal(part, start)
            part = []
            start = w
        if w < start and idx == (len(walls) - 1):
            answer += last(start, part)


    return answer

if __name__ == '__main__':
    W, H = map(int, input().split())
    inputs = [*map(int, sys.stdin.readline().split())]
    print(solution(W, H, inputs))
