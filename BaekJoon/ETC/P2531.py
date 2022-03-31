# 백준 구현 P2531 회전 초밥
import sys

def sol():
    max_val = 0
    for i in range(n-k+1):
        temp = set(sushi[i:i+k])
        result = len(temp)
        if c not in temp: result = len(temp) + 1
        if max_val < result:
            max_val = result

    for i in range(n-k+1,n):
        temp = set()
        for j in range(i,i+k):
            temp.add(sushi[(j)%n])
        result = len(temp)
        if c not in temp: result = len(temp) + 1
        if max_val < result:
            max_val = result

    return max_val

if __name__ == '__main__':
    n, d, k, c = map(int,sys.stdin.readline().split())

    sushi = []
    for i in range(n):
        sushi.append(int(sys.stdin.readline().strip()))

    print(sol())
