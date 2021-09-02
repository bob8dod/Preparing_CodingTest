def solution(answers):
    answer = []
    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]
    result = [0,0,0]
    for idx,cur in enumerate(answers):
        if cur == num_1[idx%len(num_1)]:
            result[0] += 1
        if cur == num_2[idx%len(num_2)]:
            result[1] += 1
        if cur == num_3[idx%len(num_3)]:
            result[2] += 1
    max_value = max(result)
    for idx,value in enumerate(result):
        if value == max_value:
            answer.append(idx+1)

    return answer
