# 12971 스티커모으기(2)
"""
DP로 접근하는 방식인 것은 눈치 챘으나, 첫번째 스티커를 떼냐 안떼냐를 구분하지 못하여 못품
-풀이-
기본적으로 원형이 아니라고 가정했을 때, DP로 쉽게 풀어낼 수 있음
하나씩 하나씩 원소들을 배열에 추가한다고 생각하면 쉬움.
즉, i번째 원소를 추가할 때, 이 i번째 원소를 무조건 포함하느냐 포함하지 않느냐로 dp점화식을 구성하면 됨
-> i번째 까지의 최대값 = max(i번째를 무조건 포함하는 경우(i-1은 무조건 배제, 즉 i-2까지의 최대값 + i의 값), i번째를 무조건 포함하지 않는 경우(i-1번째 까지의 최대값))
-> dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
근데 여기서 원형이기에 또
0번째 요소를 포함하느냐 포함하지 않느냐로 구분해서 풀어야됨
0 번째 요소를 포함 -> 마지막 인덱스(0번째에 붙어있는 인덱스)는 무조건 제외-> 없다고 생각하면됨
0 번째 요소를 비포함 -> 0번째 인덱스는 포함하지 않기에 0으로 두고 마지막 인덱스까지의 최대값을 고려하면 됨
"""

def solution(sticker):
    if 1 <= len(sticker) <= 3:
        return max(sticker)
    dp = [0 for _ in range(len(sticker))]
    # 첫번째 스티커를 뗀 경우 -> 마지막 스티커는 고려하면 안됨
    dp[0] = sticker[0]
    dp[1] = dp[0]
    dp[2] = dp[1]+sticker[2]
    for i in range(3, len(sticker)-1):
        dp[i] = max(dp[i-2]+sticker[i], dp[i-1]) # i를 무조건 포함 vs i를 무조건 미포함
    dp[len(sticker)-1] = dp[len(sticker)-2] # 마지막 스티커는 무조건 미포함

    # 첫번째 스티커를 떼지 않은 경우 -> 마지막 스티꺼까지 고려해야됨
    dp2 = [0 for _ in range(len(sticker))]
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-1])

    return max(dp[len(sticker)-1] , dp2[len(sticker)-1])
