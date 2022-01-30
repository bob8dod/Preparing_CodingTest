# 1254 펠린드롬 만들기 최적화
"""
앞에서 부터 차근 차근 현재 인덱스부터 끝까지의 문장이 펠린드롬인지 확인
즉, 문장의 sub 문장들이 팰린드롬인 놈을 확인하는 것
그 sub 문장이 팰린드롬이라면 사실 그 sub 문장 뒤꽁무니에 앞의 여분의 문장을 reverse 해서 팰린드롬을 만들어주면 되는 거임
ex) abede
    1. 'abede' X
    2. a 'bede' X
    3. ab 'ede' O => abedeba
"""

s=input()
for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(len(s)+i)
        break
