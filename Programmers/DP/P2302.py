# 백준 DP P2302 극장 좌석
"""
인원이 한명씩 추가될 때의 경우의 수를 따짐.
만약 12 에서 3이 추가되었다.
그럼 3의 위치를 고정시켜 생각.
만약 3이 자기 자리를 유지한다 -> 12 3 , 21 3. 즉, 1과2에서의 경우의 수를 그대로 받아옴
만약 3이 자리를 바꿨다 -> 1 32. 즉, 1에서의 경우의수를 그대로 받아옴
즉, 현재 경우의 수 = 이전 경우의수(현재 위치 고정) + 전전 경우의수(바꾼 자리를 고정)
    => dp[i] = dp[i-1] + dp[i-2]
##
DP는 이런식으로 생각하면 됨.
이전조건과 다른 상황은 무엇이며 그 상황을 어떻게 이전 값들과 연관지어 고려할 것인지에 대한
점화식을 만들어내면 됨
"""
def main():
    N = int(input())
    M = int(input())

    V = [0] + [int(input()) for _ in range(M)] +[N+1]

    dp = [1 for _ in range(N+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    total = 1
    for i in range(len(V)-1):
        length = (V[i+1] - V[i] - 1)
        total *= dp[length]

    print(total)

if __name__ == "__main__":
    main()
