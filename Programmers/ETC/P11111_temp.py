def solution(p):
    n = len(p)
    answer = [0 for _ in range(n)]
    for i in range(n):
        min_n = p[i]
        min_idx = i
        for j in range(i,n):
            if min_n > p[j]:
                min_n = p[j]
                min_idx = j
        if min_n != p[i]:
            p[i],p[min_idx] = min_n, p[i]
            answer[i] += 1
            answer[min_idx] += 1
        print(p)

    return answer
