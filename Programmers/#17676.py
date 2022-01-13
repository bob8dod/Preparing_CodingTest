# 추석 트래픽_90min
"""
먼저 시간을 ms 단위로 전부 바꿔준 후 시작시간과 끝시간을 처리시간 T를 통해 계산하여 check 배열에 저장
그 후 최대로 많이 처리한 것을 구하기 위해
각 요소들의 끝시간을 기준으로 +1s 의 구간을 설정하고
나머지 요소들이 해당 구간안에 들어오는지를 판단.
이는 4가지 경우로 나뉘어서 해결
1) 시작시간 끝시간 모두 구간안에 들어오는 경우
2) 시작시간만 구간안에 들어오는 경우
3) 끝시간만 구간안에 들어오는 경우
4) 시작시간과 끝시간의 범위가 구간을 초과하는 경우
$ 1번 가정은 사실 2,3번가정과 겹치므로 생략
결로적으로 2,3,4 가정에 해당하는 요소들에 개수를 파악
"""
def find(check):
    max_cnt = 0
    for i in check:
        cnt = 0
        for j in check:
            if i[1] <= j[0] <= i[1]+999:
                cnt+=1
                continue
            if i[1] <= j[1] <= i[1]+999:
                cnt+=1
                continue
            if j[0] < i[1] and j[1] > i[1]+999:
                cnt+=1
                continue

        if cnt > max_cnt: max_cnt = cnt
    return max_cnt


def solution(lines):
    check=[]
    for li in lines:
        t,m,s = li.split()[1].split(':')
        t, m = int(t), int(m)
        s = float(s)
        T = int((float(li.split()[2][:-1]) - 0.001)*1000)

        to_ms = int(s*1000 + m*60*1000 + t*60*60*1000)
        start_time, end_time = to_ms - T , to_ms
        check.append([start_time, end_time])

    answer = find(check)
    return answer
