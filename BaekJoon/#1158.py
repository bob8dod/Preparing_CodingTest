# 요세푸스_30min
"""
일반 list로 구현
인덱스로 접근하는 방식으로 구현
m = (m+K-1)%len(li) 로 삭제할 인덱스를 수식적으로 표현하여 구현
삭제 시 del 보다 pop이 효율적!
"""

def yose(N,K):
    li =[i for i in range(1,N+1)] #list(range(1,N+1))
    result = []
    m = 0
    while li:
        m = (m + K-1)%len(li)
        tem = li.pop(m)
        result.append(tem)

    return result

def solution():
    N, K = map(int,input().split())
    result = yose(N,K)
    print('<{}>'.format(', '.join(map(str, result))))
