def solution(numbers):
    answer=''
    numbers = list(map(str,numbers))
    max_len = sorted(map(len, numbers))[-1]
    compares = []
    for i in range(len(numbers)):
        num = str(numbers[i])*4
        new_num = [i, int(num[:max_len])]
        compares.append(new_num)
    result = sorted(compares, key=lambda x:x[1], reverse=True)

    for idx, v in result:
        answer+=numbers[idx]

    if answer[0] == '0':
        return '0'
    return answer
