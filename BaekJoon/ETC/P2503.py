# 백준 구현 P2503 숫자 야구
"""
나의 실수 :
- 123에서 1strike 1ball 일때 생길 수 있는 모든 경우를 구하고 그 구한 경우에서 다음으로 넘어가 반복하려 함
    -> 굉장히 비효율적이고 코드가 복잡해짐
풀이 :
애초에 모든 3자리의 수를 구해놓은 다음
각 조건에 해당하는 애들만 필터링해주면 간편함

즉, 3자리 순열을 구하고
그 모든 경우의 수들에서
1. 123일 때의 1s 1b 인 애들만 걸러냄
2. 그 걸러낸 상태에서 356에 대해 1s 0b 인 애들만 걸래냄
3. 위 과정 각 조건에 맞게 계속해서 반복...
=> 결국 해당하는 모든 조건에 맞는 수들만 남게 되는 것
"""

from itertools import permutations

def solution(N,li):
    nums = list('123456789')
    candidates = permutations(nums, 3)

    for i in range(N):
        q, s, b = li[i]
        q = list(str(q))
        answer = []
        for cand in candidates:
            curr_s = 0
            curr_b = 0
            for j in range(3):
                for k in range(3):
                    if q[j] == cand[k]:
                        if j == k: curr_s+=1
                        else: curr_b += 1

            if curr_s == s and curr_b == b:
                answer.append(cand)
        candidates = answer.copy()

    return len(candidates)


if __name__ == '__main__':
    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]
    print(solution(N, li))
