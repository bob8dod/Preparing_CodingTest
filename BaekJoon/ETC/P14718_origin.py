# BaekJoon P14718 "빗물" (구현, 시뮬레이션 | G5)
"""
---[실수]---
마지막단에 대한 처리를 못했음
---[부족한 점]---
구현, 시뮬레이션 등에 너무 약함 -> 연습 필요
---[풀이]---
처음 벽부터 훑어가면서 시작점보다 크거나 같으면 끊고 계산
마지막 단에 대해선 따로 처리
---[비고]---
"""
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
