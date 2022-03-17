# 백준 HEAP P11286 절댓값 힙
"""
기본적인 heapq를 사용해서 풀이진행.
heapq는 2차원으로도 가능하다는 점을 이용.
가장 먼저 0인덱스를 기준으로 heap정렬을 진행하고,
만약 동일한 숫자라면 1인덱스를 기준으로 정렬을 진행.
so, 0인덱스에는 절댓값을, 1인덱스에는 원본값을 저장하며
heap에 넣어줌.
[참조]
import heapq
heapq.heappush(list,[abs(value),value])
heapq.heappop(list)
$ heapq의 모든 과정은 inplace!
"""
import heapq
import sys

def main():
    N = int(sys.stdin.readline().strip())
    order=[]
    for _ in range(N):
        order.append(int(sys.stdin.readline().strip()))

    q = []
    for x in order:
        if x != 0:
            heapq.heappush(q, [abs(x), x])
        elif x == 0 and q:
            ab, origin = heapq.heappop(q)
            print(origin)
        else:
            print(0)


if __name__=='__main__':
    main()
