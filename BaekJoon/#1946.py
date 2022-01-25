#1946_신입사원 (Greedy)
"""
맨 처음에는 서류 점수와 면접점수를 따로 저장해서
이들에 대해서 각각 판단함 -> 시간초과

정답은 결국 먼저 서류점수로 정렬 (혹은 index를 서류점수로 저장 -> 저장 시 자동 정렬됨) 후
면접 점수로 사원 채용을 판단.
여기서 중요한 것은 이미 서류점수로 정렬되었기 때문에 이미 1등을 제외하고는 모두 서류점수로써 1차위기가 옴
이제 그 정렬된 순서를 기준으로 면접 순위는 그 이전 인덱스의 놈들보다 높아야지만 채용 가능
이를 인덱스 하나하나 넘어가며 그 전까지의 최고 순위를 기록하고
이보다 높다면 그 값을 변경해주고 cnt해줌.
"""
import sys
def check(n,emplo):
    cnt = 1
    front_max = emplo[1]
    for i in range(1,n+1):
        if front_max == 1: return cnt
        if emplo[i] < front_max:
            cnt+=1
            front_max = emplo[i]

    return cnt

def solution():
    t = int(input())
    for i in range(t):
        n = int(input())
        emplo = [0 for _ in range(n+1)]
        for j in range(n):
            p, i = map(int,sys.stdin.readline().split())
            emplo[p] = i

        print(check(n, emplo))
    return

solution()
