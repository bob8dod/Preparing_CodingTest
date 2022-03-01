# 프로그래머스 월간 코드 챌린지 시즌2 P76502 괄호 회전하기
"""
rotate 하면서 
stack을 통해 괄호가 올바른지 체크.
"""
def solution(s):
    answer = 0
    if len(s) %2 != 0:
        return answer

    for i in range(len(s)):
        stk = []
        for j in range(i,i+len(s)):
            # s[j%len(s)]
            if s[j%len(s)] == ')':
                if len(stk)!= 0 and stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(')')
                    break
            elif s[j%len(s)] == ']':
                if len(stk)!= 0 and stk[-1] == '[':
                    stk.pop()
                else:
                    stk.append(']')
                    break
            elif s[j%len(s)] == '}':
                if len(stk)!= 0 and stk[-1] == '{':
                    stk.pop()
                else:
                    stk.append('}')
                    break
            else:
                stk.append(s[j%len(s)])

        if len(stk)==0:
            answer += 1

    return answer
