# 프로그래머스 P12979 기지국 설치
"""
N이 최대 200억이기에 절대 모든 원소를 훑는 과정은 불가하다는 것을 인지.
주어진 station의 시작과 끝을 이용해 전파가 닿지 않는 구간을 설정
근데 설정하는 과정에서 바보같이 사고력 부족으로 이상하게 품.
결론적으로 처음과 끝은 중간과는 다른 개념이라 생각하고 접근하고
중간에 있는 애들은 전파가 닿는 것이 아닌 전파가 닿지 않는 애들을 기준으로 풀어야 됨
-> start가 현재 인덱스의 끝점 , end가 다음 인덱스의 시작점
"""
def solution(n, stations, w):

    check = []
    if stations[0]-w-1 >= 1:
        check.append([1, stations[0] - w - 1])

    for i in range(len(stations)-1):
        start = stations[i] + w + 1
        end = stations[i+1] -w -1
        if start <= end : check.append([start, end])

    if stations[-1] + w + 1 <= n:
        check.append([stations[-1] + w + 1, n])

    cnt = 0
    div = (2 * w + 1)
    for ch in check:
        length = ch[1] - ch[0] + 1
        if length % div == 0: cnt += length // div
        else: cnt += length // div + 1

    return cnt


print(solution(11, [4, 11], 1))
