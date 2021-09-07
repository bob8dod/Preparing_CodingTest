def solution(n, lost, reserve):
    after_reserve = [i for i in reserve if i not in lost]
    after_lost = [i for i in lost if i not in reserve]
    for r in after_reserve:
        if r-1 in after_lost:
            after_lost.remove(r-1)
        elif r+1 in after_lost:
            after_lost.remove(r+1)
    return n - len(after_lost)

print(solution(5, [2, 3, 4], [3, 4, 5]))
