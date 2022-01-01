# 그룹 단어 체커
"""
먼저 단어 속 문자들이 연속한 순간이냐 아니냐 두가지로 나누어서 판단 진행
연속적인 단어일 경우 그냥 바로 다음 인덱스로 넘어가도록 설정
연속적인 단어가 아닐 경우 딕셔너리를 통해 이전에 나왔던 단어인지 판단
이를 통해 0 or 1 반환
"""

def isGroup(word):
    check={word[0]:True}
    for i in range(1,len(word)):
        if word[i-1] == word[i]: continue
        if word[i] in check: return 0
        check[word[i]] = True
    return 1

def solution():
    N = int(input())
    cnt = 0
    for i in range(N):
        word = input()
        cnt+=isGroup(word)
    return cnt
