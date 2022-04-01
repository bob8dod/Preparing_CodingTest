# 백준 Two-Pointer, Windowing P15961 회전초밥
"""
그 순간마다 list slicing을 통해 count하는 것이 아닌, -> (이렇게 하면 시간 초과 _ N*k 만큼 걸림)
tow pointer와 windowing을 통해서 해결. -> (N만큼의 시간만 걸림)
가장 먼저 첫번째 시작 (포인터의 위치 조정)에서 cnt를 해주고, end pointer의 위치를 조정해줌 ->  k 크기의 윈도우 설정
그리고 각 N번마다 윈도우에 나가고 들어오는 놈들이 기존에 있는 놈인지 없는 놈인지 판단해서 cnt를 늘리거나 줄여줌
마지막으로 각 반복 시 C라는 공짜 번호를 가지고 있는지 판단해서 있으면 더하지말고, 없으면 더해줌 (더해줬다면 다음 cnt를 위해 뺴줌)
각 반복 시 나오는 결과 cnt를 비교하여 가장 큰 값의 cnt를 max_cnt로 지정
"""
import sys
def solution(N,d,k,c,li):
    fin = li + [li[i] for i in range(0,k-1)]
    memo = [0 for _ in range(d+1)]
    e = 0

    cnt = 0
    for _ in range(k):

        memo[fin[e]] += 1
        if memo[fin[e]] == 1:
            cnt += 1
        e += 1
    if memo[c] == 0:
        cnt += 1

    max_cnt = cnt
    if memo[c] == 0:
        cnt -= 1

    for i in range(1,N):
        memo[fin[i-1]] -= 1
        if memo[fin[i-1]] == 0:
            cnt -= 1
        memo[fin[e]] += 1
        if memo[fin[e]] == 1:
            cnt += 1
        if memo[c] == 0:
            cnt += 1

        max_cnt = max(max_cnt, cnt)
        if memo[c] == 0:
            cnt -= 1

        e += 1

    print(max_cnt)



if __name__ == '__main__':
    N, d, k, c = map(int,sys.stdin.readline().split())
    li = []
    for _ in range(N):
         li.append(int(sys.stdin.readline().strip()))
    solution(N,d,k,c,li)
