# BaekJoon P5430 AC Gold5
"""
[풀이]
시간 복잡도를 개선하기 위해 포인터로 접근.
매 반복마다 현재 list의 길이를 측정.
물론 처음부터 len이 0인애도 있지만, 변환 과정에서도 0이 있을 수 있기에 반복 과정에서 0 처리 필요.
만약 현재 order가 R이다 -> 포인터의 위치 변경 (0->length-1, length-1 -> 0)
                D이다 -> 포인터 위치의 요소 삭제 (deque 이용)
                        그 후 포인터의 위치 변경 (left에서 삭제할 경우는 그냥 유지, right에서 삭제할 경우는 포인터를 한칸 왼쪽으로)
[실수]
order가 D일 때,
pointer의 위치에 따라 삭제하는데
이때 맨 왼쪽 요소(index:0)을 삭제할 때는 pointer의 변동이 필요없음.
deque를 통해 popleft를 해주면 삭제 후 맨 첫번재 요소는 똑같이 인덱스가0임. 즉, p도 0으로 유지해 주면 됨
"""

from collections import deque

results = []

def logic(li, order):
    p = 0
    for s in order:
        length = len(li)
        if length == 0:
            if s == 'D':
                results.append('error')
                return
            continue

        if s=='R':
            if p == 0:
                p = length-1
            else:
                p = 0

        else:
            if p == length-1:
                li.pop()
                p -= 1
            else: # p == 0
                li.popleft()

    result = list(li)
    if p == len(li)-1:
        result.reverse()
    answer = '['
    answer += ','.join(result)
    answer += ']'
    results.append(answer)


def solution():
    k = int(input())
    for _ in range(k):
        order = input()
        n = int(input())
        liStr = input()[1:-1].split(",")
        li = deque(liStr)
        if n==0:
            li = []

        logic(li, order)

    for result in results:
        print(result)

if __name__ == '__main__':
    solution()
