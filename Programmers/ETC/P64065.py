# 프로그래머스 2019 카카오 개발자 겨울 인턴십 P64065 튜플
"""
주어진 문자열에서 숫자에 해당하는 것들만 받아온 후
그 숫자들만 담겨 있는 배열을 길이순으로 sort하고
각각의 배열의 요소의 차이를 구해 int 변환 후 저장.
"""
def solution(s):
    
    result = s[2:-2].split('},{')
    result.sort(key=len)

    answer = []
    answer.append(int(result[0][0]))
    for i in range(len(result)-1):
        tem_set = set(result[i + 1]) - set(result[i])
        answer.append(int(list(tem_set)[0]))
    return answer
