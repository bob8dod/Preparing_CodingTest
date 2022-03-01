# 프로그래머스 월간 코드 챌린지 시즌2 P77885 2개 이하로 다른 비트
def f(x):
    if x % 2 == 0:  # 짝수면 비트 끝 자리가 무조건 0이기 때문에 한 비트 차이나는 가장 작은 값은 +1한 값
        return x + 1

    else:
        y = '0' + bin(x)[2:]
        idx = y.rfind('0')
        y = list(y)
        y[idx] = '1'
        y[idx + 1] = '0'

        return int(''.join(y), 2)

def solution(numbers):
    answer = [f(int(i)) for i in numbers]

    return answer
