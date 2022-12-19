answer = 0

def back_tracking(curr_idx, curr_hp, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = max(cnt, answer)
    
    for i, [needed, cost] in enumerate(dungeons):
        if not visited[i] and curr_hp >= needed:
            visited[i] = 1
            back_tracking(i, curr_hp - cost, cnt+1, dungeons, visited)
            visited[i] = 0

def solution(k, dungeons):
    n = len(dungeons)
    visited = [0 for _ in range(n)]
    for i, [needed, cost] in enumerate(dungeons):
        if k >= needed:
            visited[i] = 1
            back_tracking(i, k - cost, 1, dungeons, visited)
            visited[i] = 0
    
    return answer
