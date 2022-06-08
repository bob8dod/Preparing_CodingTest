# BaekJoon P1759 암호만들기 (구현, 부르트포스 / Gold5)
"""
[실수]
for 문이 한 3개 이상 되니깐 코드를 어디다 넣어야 되는지 놓침.
이런 부분은 좀 단계적으로 생각해서 진행해야 될듯

[특이 점]
combinations 와 같은 제너레이터는 변수에 할당하고 한번밖에 사용 못함!!
그니깐 combinations을 사용할 때는 변수에 할당하지 말고 바로 사용하든가
변수에 할당할 때는 list와 같은얘로 generic, iterator를 풀어줘야됨!

[풀이]
먼저 자음과 모음에 해당하는 애들을 분리하고
자음에서는 2개, 모음에서는 1개를 뽑은 후
가능한 모든 문자열을 생성. (뽑고 남은 문자들을 끼워맞추는 형식으로)
그후 각 문자열을 정렬하고
마지막으로 그 결과 리스트를 정렬하여 반환
=> 사실 모든 문자열에 대한 combination 진행 후 모음 자음 개수로 판별하는게 훨 남

"""

# 최소 1개의 모음, 최소 2개의 자음, 중복X
# 오름차순

from itertools import combinations


def solution(l, c, arr):
    aeiou = {i for i in 'aeiou'}
    mo, ja = set(), set()
    for a in arr:
        if a in aeiou: mo.add(a)
        else: ja.add(a)

    # ja_order = list(combinations(ja, 2))
    results = set()
    for m in mo:
        for j1,j2 in combinations(ja, 2): # ja_order
            rest = [mt for mt in mo if mt != m]
            rest.extend([jt for jt in ja if jt != j1 and jt != j2])
            rest_order = combinations(rest,l-3)
            for r_o in rest_order:
                result = m + j1 + j2
                for r in r_o:
                    result += r
                results.add(''.join(sorted(result)))

    return sorted(results)

if __name__ == '__main__':
    l, c = map(int, input().split())
    arr = list(input().split())
    answer_li = solution(l, c, arr)
    for answer in answer_li:
        print(answer)
