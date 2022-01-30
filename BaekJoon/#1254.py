# 1254 팰린드롬 만들기_40min
"""
먼저 뒤에서 문장의 뒷 글자부터 팰린드롬의 중앙, 즉 기준이 될 수 있는지 확인 (tem) - ab'c'ba
근데 여기서 중앙이 되는 글자 없이 팰린드롬이 되는 경우를 추가. (tem2) - abc/cba
그에 맞는 계산 추가
"""

def solution(s):
    answer = 0
    to_end = len(s)//2
    for i in range(len(s)-1, to_end-1, -1):
        tem = s[i+1:]
        tem2 = s[i:]
        if tem2 == ''.join(reversed(s[i-len(tem2):i])):
            answer = len(s) + len(s) - (len(tem2) * 2)
        elif tem == ''.join(reversed(s[i-len(tem):i])):
            answer = len(s) + len(s) - (len(tem)*2+1)

    return answer
