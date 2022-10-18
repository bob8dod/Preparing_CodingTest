# BaekJoon P2839 "설탕 배달" (그리디 | S4)
"""
---[실수]---
---[부족한 점]---
그냥 모든 애들을 search 및 answer 를 비교해서 return 하려고 했지만,
사실 3이 0인 것부터 search 해서 n 이랑 같은 수가 나오면 바로 반환해주면 됨 -> 그리디
=> 최소 개수는 항상 3이 적고, 5가 커야 최소가 되므로
<<수정 전>>
for f in range(max_five+1):
    for t in range(max_three+1):
        result = t*3 + f*5
        if result == n:
            answer = min(answer, t+f)
<<수정 후>>
for t in range(max_three+1):
    for f in range(max_five+1):
        result = t*3 + f*5
        if result == n:
            return t+f
---[풀이]---
---[비고]---
풀이 시간 : 6m
"""

def solution(n):
    max_five = n//5
    max_three = n//3
    for t in range(max_three+1):
        for f in range(max_five+1):
            result = t*3 + f*5
            if result == n:
                return t+f
    return -1
if __name__ == '__main__':
    N = int(input())
    print(solution(N))
