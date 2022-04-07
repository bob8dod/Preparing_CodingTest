# 프로그래머스 2020 카카오 인턴십 STACK P67257 수식 최대화
"""
일반적인 노가다 구현으로 진행했으나 틀림,
결국 Stack을 이용해서 원하는 연산자가 나올 때마다 pop해서 계산을 진행해 줘야 했음
STACK!!!
"""
import re
from itertools import permutations

def calc(a,b,op):
    if op =="*":
        return a*b
    elif op =='+':
        return a+b
    elif op == '-':
        return a-b

def solution(expression):
    nums = re.findall('\d+',expression)
    operates = re.findall('[*+-]',expression)
    result = []
    for i in range(len(operates)):
        result.append(nums[i])
        result.append(operates[i])
    result.append(nums[-1])

    answer = 0
    temp = set(operates)

    for per in permutations(temp,len(temp)):
        tem_result = result.copy()
        for op in per:
            stk = []
            i = 0
            while i < len(tem_result):
                if not tem_result[i].isdigit() and tem_result[i] == op:
                    stk.append(str(calc(int(stk.pop()), int(tem_result[i+1]), op)))
                    i+=2
                else:
                    stk.append(tem_result[i])
                    i+=1
            tem_result = stk.copy()
        answer = max(abs(int(tem_result[0])),answer)

    return answer

print(solution("50*6-3*2"))
