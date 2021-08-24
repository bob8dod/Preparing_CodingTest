import heapq
import sys


# 시간을 기준으로 해당 시간에 들어온 요청 중 가장 작은 가동시간을 가지고 있는 디스크를 선택
def solution(jobs):
    time = 0  # 시간
    total = 0  # 평균 내기 위한 총합
    heap = []  # 그 시점의 가장 작은 가동시간을 판단하기 위해 heap사용
    check = 0  # 모든 디스크를 둘러봤는지 판단하기 위한
    N = len(jobs)  # 총 디스크의 수

    while True:
        # 모든 디스크를 둘러봤으면 반복문에서 나가기
        if check == N:
            break
        # 현재 시점까지 들어온 요청들을 heap에 추가
        for i in range(N):
            if jobs[i][0] <= time:  # 현재 시점안에 들어온 요청인지 판단
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])  # 가동시간과 요청시간을 함께 저장 (추후 계산에 이용)
                jobs[i][0] = sys.maxsize  # 현재 추가한 디스크는 이후에 비교대상이 아니므로 제외시켜줌
        if not heap:  # 요청이 아무것도 들어오지 않았다면
            time += 1  # 다음 시간
            continue
        min = heapq.heappop(heap)  # 현재 heap에 들어온 것 중 최소 가동시간을 추출
        check += 1  # 가동 디스크 수 추가
        time += min[0]  # 가동시간
        total += time - min[1]  # 요청 ~ 가동 끝

    return int(total / N)  # 평균 값 도출
