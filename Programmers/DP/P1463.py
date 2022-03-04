# 백준 DP P1463 1로 만들기
"""
기본적인 DP 문제.
1로 만들기를 거꾸로 생각하여 1에서 N으로 만들기로 편리하게 품.
DP는 항상 이전값들을 어떻게 이용할건지에 대한 고민만 잘 하면 됨.
"""
def main():
   N = int(input())
   dp = [i-1 for i in range(N+1)]
   dp[1] = 0
   for i in range(2,N+1):
       two = dp[i//2]+1 if i%2==0 else i-1
       three = dp[i//3]+1 if i%3==0 else i-1
       dp[i] = min(dp[i-1]+1,two,three)

   print(dp[N])



if __name__ == "__main__":
    main()
