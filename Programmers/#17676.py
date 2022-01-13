# 추석트래픽
def calc_time(tms, T):
    T = float(T) - 0.001
    t,m = map(int, tms.split(':')[:-1])
    s = float(tms.split(':')[-1])
    end_time = tms
    if s < T:
        if m == 0:
            t = t -1
            m += 60
        m = m-1
        s+= 60

    s -= T

    start_time = '{}:{:02d}:{:.3f}'.format(t,m,s)
    return start_time, end_time

def find(check):
    for i in check:
        check_time = i[1] + 0.999



def solution(lines):
    check = []
    for li in lines:
        li_sp = li.split()
        tms = li_sp[1]
        T= li_sp[2][:-1]

        s,e = calc_time(tms,T)
        check.append([s, e])

    answer = find(check)
    return answer
