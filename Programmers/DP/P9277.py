def solution(money, costs):
    dp = [0 for _ in range(money+1)]
    mon = [1,5,10,50,100,500]
    cost = [[key,val] for key,val in zip(mon,costs)]

    for m,c in cost:
        if m == 1:
            dp = [c*i for i in range(money+1)]
            continue
        for i in range(m,money+1):
            tem = dp[i-m] + c
            dp[i] = min(tem,dp[i])

    answer = dp[-1]
    return answer
