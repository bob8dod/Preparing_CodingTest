def solution(citations):
    citations.sort(reverse=True)
    max_n = citations[0]
    result = []
    for i in range(max_n+1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
            else:
                break
        result.append(count)

    for i,v in enumerate(result):
        if i>v:
            return i-1
    else:
        return len(result)-1
