def solution(n, lost, reserve):
    lost = set(sorted(lost))
    reserve = set(sorted(reserve))
    same = lost & reserve
    lost = list(lost - same)
    reserve = list(reserve - same)

    rem_idx = []
    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            idx = reserve.index(lost[i] - 1)
            rem_idx.append(i)
            reserve.pop(idx)
        elif lost[i] + 1 in reserve:
            idx = reserve.index(lost[i] + 1)
            rem_idx.append(i)
            reserve.pop(idx)

    answer = n - (len(lost) - len(rem_idx))

    return answer
