# 프로그래머스 월간 코드 챌린지 시즌1 P70129 이진 변환 반복하기
"""
10진수를 2진수로 변환 -> bin
거기서 숫자만 가져오기 [2:]
"""
def solution(s):
    time = 0
    cnt = 0
    while s != '1':
        time += 1
        before = len(s)
        after = s.count('1')
        cnt += (before - after)
        s = bin(after)[2:]

    return [time,cnt]
