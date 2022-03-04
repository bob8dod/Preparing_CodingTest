# 백준 분할정복 P1992 쿼드트리
"""
말 그대로 쿼드 분할 정복.
이전에 풀었던 분할정복에서 반환값만 조금 다른 버전.
분할 정복할 떄 쓰이는 재귀 함수의 인자값들이 어떤게 들어가는지 항상 주의.
또한, 분할정복 및 재귀 함수는 항상 그려가면서 판단필요!!!!
"""
def con(i,j,n):

    if n == 1:
        return str(gmap[i][j])

    term = n // 2
    div = [[i,j], [i,j + term], [i + term, j], [i + term, j + term]]
    total = ''
    for d in div:
        total += con(d[0],d[1],n//2)

    if total == '0000': return '0'
    elif total == '1111': return '1'
    else:
        return '(' +total+ ')'



def main():
    global N, gmap
    N = int(input())
    gmap = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        tem = input()
        for j in range(N):
            gmap[i][j] = int(tem[j])

    print(con(0,0,N))

if __name__ == "__main__":
    main()
