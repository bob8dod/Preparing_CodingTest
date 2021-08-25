def solution(genres, plays):
    idx_dict = dict()
    count_dict = dict()
    answer = []
    idx = 0
    for k, v in zip(genres, plays):
        idx_dict[idx] = [k, v]
        idx += 1
    for k, v in idx_dict.values():
        if k not in count_dict.keys():
            count_dict[k] = v
        else:
            count_dict[k] += v
    count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    idx_dict = sorted(idx_dict.items(), key=lambda x: x[1][1], reverse=True)

    for cate, _ in count_dict:
        j = 0
        for idx, value in idx_dict:
            if j == 2:
                break
            if value[0] == cate:
                answer.append(idx)
                j += 1
        
    return answer
