from itertools import permutations

def check(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

def solution(numbers):
    numbers = list(numbers)
    per = []
    for i in range(1,len(numbers)+1):
        per.extend(list(permutations(numbers, i)))
    result_nums = set()
    for i in range(len(per)):
        temp = ''
        for j in range(len(per[i])):
            temp += per[i][j]
        result_nums.add(int(temp))

    cnt = 0
    for num in result_nums:
        if num >1 and check(num):
            cnt+=1
    return cnt
