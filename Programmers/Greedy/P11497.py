# 백준 Greedy P11497 통나무 건너뛰기
"""
가장 큰 놈을 기준으로 양쪽으로 쭉 펼쳐주면 됨.
즉, 산 모양으로 통나무를 세워주면 옆에 놈들과의 차이가 가장 적어짐.
"""
from collections import deque

def check(N,li):
    result=deque()
    li.sort(reverse=True)
    result.append(li[0])
    for i in range(1,N,2):
        result.append(li[i])
        if i+1 < len(li): result.appendleft(li[i+1])

    answer = 0
    for i in range(1, N):
        answer = max(answer, abs(result[i-1] - result[i]))

    return answer

def main():
    T = int(input())
    answer = []
    for t in range(T):
       N = int(input())
       li = list(map(int,input().split()))
       answer.append(check(N,li))
    for a in answer:
        print(a)

if __name__ == "__main__":
    main()
