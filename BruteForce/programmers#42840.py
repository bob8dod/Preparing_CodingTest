from collections import defaultdict

def solution(answers):
    answer = []
    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]
    result = defaultdict(int)
    for i in range(len(answers)):
        cur = answers[i]
        if cur == num_1[i%len(num_1)]:
            result[1] += 1
        if cur == num_2[i%len(num_2)]:
            result[2] += 1
        if cur == num_3[i%len(num_3)]:
            result[3] += 1
    temp = sorted(result.items(), key= lambda x:x[1], reverse=True)
    max_value = temp[0][1]
    for i,v in result.items():
        if v == max_value:
            answer.append(i)

    return sorted(answer)
