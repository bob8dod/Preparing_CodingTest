# 프로그래머스 월간 코드 챌린지 P77886 110 옮기기
"""
stack으로 풀지 않고 string 그 자체로 자르고 이어붙이고 하면 시간초과.
stack으로 풀 때, 110이 나올 때 마다 cnt를 1씩 추가해주며 110을 제거
그리고 그 cnt 만큼 110을 추가해줌.
추가해 줄때, 기존의 stack에서 pop을 할때 0이 나오면 그 뒤로 바로 110을 붙여줌
-> 0 이전으로는 110이 들어갈 자리가 없음. (0001'0', 0010101'0', .. )
"""
from collections import deque

def solution(ss):
    answer = []
    for s in ss:
        cnt = 0
        stack = []
        for c in s:
            # 110
            if c == '0' and stack[-2:] == ['1','1']:
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append(c)

        result = deque()
        while stack:
            c = stack[-1]
            if c =='0': # 0 이전으로는 110이 들어갈 곳이 없기 때문
                break
            else:
                result.appendleft(stack.pop())

        while cnt:
            result.appendleft('0')
            result.appendleft('1')
            result.appendleft('1')
            cnt-=1

        while stack:
            result.appendleft(stack.pop())

        answer.append(''.join(result))

    return answer

print(solution(["110001","100111100","0111111010"]))
