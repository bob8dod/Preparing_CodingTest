# 가지고 노는 1
"""
중요X _ 수학적인 문제
(i*10+1)%N == ((i%N)*10+1)%N 과 똑같다는 사실을 이용
수의 크기를 줄여 연산 부담을 덜해줌. -> 시간 초과 해결
"""
def solution(N):
    if N%2==0 or N%5==0:
        return -1
    i = 1
    cnt = 1
    while i%N != 0:
        i = (i%N)*10+1
        cnt+=1

    return cnt

N = int(input())
print(solution(N))
