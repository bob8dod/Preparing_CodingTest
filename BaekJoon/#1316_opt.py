# 그룹 단어 체크 최적화
"""
기존의 단어의 리스트와
단어가 처음 나타난 순서를 유지한채 정렬한 새로운 단어 리스트를 비교
이렇게 되면 연속되지 않은 문자를 검출해낼 수 있음
"""

def solution():
    N= int(input())
    result=0
    for i in range(N):
        word = input()
        if list(word) == sorted(word, key=word.find): result += 1
    return result
