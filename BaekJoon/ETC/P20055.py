# BaekJoon P20055 "컨베이어 밸트 위의 로봇" (구현 | Gold5)
"""
[실수]
X

[부족한 점]
투 포인터로 생각하여 좀 오래 걸린듯 -> 풀긴 풀었지만 투포인터로 인덱스로 접근하려고 고민하다 보니 시간이 꽤 걸림
하지만 이 문제는 deque를 사용했으면 더 빨리 풀 수 있었음
투포인터를 움직여서 벨트가 도는 것은 구현 -> deque.rotate(1) 로 쉽게 구현 가능
해당 요소의 개수 구하기 -> deque.count(0) 로 쉽게 구현 가능
또한 deque가 시간복잡도에서 우위!

=> 리스트를 막 돌리고, 없애고 .. 이렇게 자유롭게 가지고 놀고 싶다면 deque를 사용하자!
[풀이]
투포인터 개념 사용 (deque로도 풀이 가능)
직접 리스트의 요소들을 움직이는 것이 아닌
요소를 가르키는 포인터를 움직이는 개념으로 접근. -> 투포인터
s : 올리는 위치, e : 내리는 위치
해당 개념으로 조건 1,2,3,4를 구현
 - 조건 1,2 는 이동이 포함되어 있기 때문에 항상 마지막 위치 확인 필요!
"""
# 이동 가능 조건 : 내구성 1 이상 and 빈 자리
import sys
from collections import deque

def solution(n,k,li): # 투 포인터
    s, e = 0, n-1
    ro = [0 for _ in range(len(li))]
    answer = 0
    while True:
        answer += 1
        # 1
        s = (s-1) % (2*n)
        e = (e-1) % (2*n)
        if ro[e]: ro[e] = 0 # 내리는 위치의 로봇 떨구기

        # 2
        i = e - 1
        while i != s:
            next = (i+1) % (2*n)
            if ro[i] and li[next] >= 1 and ro[next] == 0:
                li[next] -= 1
                ro[next] = 1
                ro[i] = 0
            i = (i-1) % (2*n)
        if ro[e]: ro[e] = 0  # 내리는 위치의 로봇 떨구기

        # 3
        if li[s] != 0:
            ro[s] = 1
            li[s] -= 1

        #4
        cnt = 0
        for val in li:
            if val == 0: cnt+=1
        if cnt >= k:
            break

    return answer

def solution2(n,k,li): # deque 풀이
    d_li = deque(li)
    ro = deque([0 for _ in range(n)])
    answer = 0
    while True:
        answer += 1
        # 1
        d_li.rotate(1)
        ro.rotate(1)
        if ro[-1]: ro[-1] = 0 # 내리는 위치의 로봇 떨구기
        # 2
        for i in range(n-1,0,-1):
            next = i+1
            if ro[i] and d_li[next] >= 1 and ro[next] == 0:
                d_li[next] -= 1
                ro[next] = 1
                ro[i] = 0
        if ro[-1]: ro[-1] = 0  # 내리는 위치의 로봇 떨구기
        # 3
        if d_li[0] != 0:
            ro[0] = 1
            d_li[0] -= 1
        # 4
        if d_li.count(0) >= k:
            break

    return answer

if __name__ == '__main__':
    n, k = map(int, input().split())
    li = list(map(int,sys.stdin.readline().split()))
    print(solution2(n,k,li))
