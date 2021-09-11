from collections import defaultdict

def solution(id_list, report, k):
    answer_dict = { id:0 for id in id_list}
    singo_dict = defaultdict(set)
    for r in report:
        singoer, singoed = r.split()[0], r.split()[1]
        singo_dict[singoed].add(singoer)

    for singoed, singoer in singo_dict.items():
        if len(singoer) >= k:
            for id in singoer:
                answer_dict[id]+=1
    answer = [v for id,v in answer_dict.items()]
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
