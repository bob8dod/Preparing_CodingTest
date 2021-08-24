import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    turn = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        turn += 1
        new_elem = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new_elem)
        
    return turn
