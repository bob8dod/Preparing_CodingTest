# 백준 Greedy P6064 카잉 달력
"""
먼저 x가 해당 조건에 맞게 가질 수 있는 해를 구하면서
각 해가 y의 조건에도 부합하는지 판단.
"""
import sys
from math import gcd

def kaing(m,n,fx,fy):
    day = fx
    lcm = m*n//gcd(m,n)
    while day <= lcm:
        if (day-fy)%n == 0:
            return day
        day += m

    return -1


def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        print(kaing(M, N, x, y))


if __name__ == "__main__":
    main()
