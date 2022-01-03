# 요세푸스 deque 버전 (일반 list보다 효율성은 떨어짐)
"""
덱(dequeque)로 푼 버전
deque의 rotate를 통해 삭제할 인덱스 전까지 요소들을 뒤로 넘겨줌 -> rotate
그 후 popleft로 제거. (deque 는 원하는 인덱스를 pop하는 기능 없음)
"""

from collections import deque
def yose(li,K):
    dq = deque(li)
    result = []
    while dq:
        dq.rotate(-(K-1))
        result.append(dq.popleft())

    return result

def solution():
    N, K = map(int,input().split())
    result = yose(list(range(1,N+1)),K)
    print(f'<{str(result)[1:-1]}>')
