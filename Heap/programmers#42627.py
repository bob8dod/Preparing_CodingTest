import heapq
import sys

def solution(jobs):
    time = 0
    total = 0
    heap = []
    check = 0
    N = len(jobs)
    while True:
        if check == N:
            break
        for i in range(N):
            if jobs[i][0] <= time:
                heapq.heappush(heap, [jobs[i][1],jobs[i][0]])
                jobs[i][0] = sys.maxsize
        if not heap:
            time += 1
            continue
        min = heapq.heappop(heap)
        check += 1
        time += min[0]  # 가동시간
        total += time - min[1]  # 요청 ~ 가동 끝

    return int(total / N)
