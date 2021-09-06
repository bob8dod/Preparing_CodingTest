def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost = set(lost)
    reserve = set(reserve)
    same = lost & reserve
    lost-=same
    reserve-=same
    lost = list(lost)
    reserve = list(reserve)
    rem_idx = []
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            idx = reserve.index(lost[i]-1)
            rem_idx.append(i)
            reserve.pop(idx)
        elif lost[i]+1 in reserve:
            idx = reserve.index(lost[i]+1)
            rem_idx.append(i)
            reserve.pop(idx)


    answer = n-(len(lost)-len(rem_idx))

    return answer
