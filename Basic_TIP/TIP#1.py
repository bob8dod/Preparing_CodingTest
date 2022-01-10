# A^B%C 를 더 빠르게. -> 얘는 O(B)임
# 거듭제곱을 거듭제곱 간의 곱으로 표현
def pow_custom(a, b, c):  # A^B%C
    result = 1
    while b:
        if b % 2 == 1: result *= a
        a = a * a % c
        b //= 2
    return result


# 최대공약수 GCD(A,B)
# ver1 _ 앞으로 진행(1부터 확인) -> 일반적인 풀이
def gcd1(a, b):
    result = 0
    for i in range(min(a, b)):
        if a % i == 0 and b % i == 0: result = i
    return result


# ver2 _ 뒤로 진행(min(a,b)부터 체크) -> 더 빠르게 진행하기 위함
def gcd2(a, b):
    result = 0
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return result


# ver3 _ 유클리드 호제법 -> GCD(A,B) = GCD(B,A%B)
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


# 최소공배수 LCM(A,B) = (A*B)/GCD(A,B)
def lcm(a, b):
    return a * b / gcd(a, b)


# 소수 판별
def isPrime(N):
    i=2
    while i*i <= N:
        if N%i==0: return False
        i+=1
    return True


# 소인수 분해 O(NloglogN)
def era(N):
    check, prime = [False for _ in range(N+1)], []
    for i in range(2,N+1):
        if check[i] == True: continue
        prime.append(i)
        for j in range(i*i, N+1, i):
            check[j] = True
    return check, prime
