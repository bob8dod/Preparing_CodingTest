order_t = [[0,1],[1,0],[0,-1],[-1,0]]
check_t = ['j','i','-j','-i']

def search_true(gmap, curr, idx, n, cnt, turn):
    i, j = curr
    gmap[i][j] = cnt

    if n%2==0 and (n//2-1 <= i <= n//2 and n//2 -1 <= j <= n//2):
        return
    if n % 2 != 0 and (i == n//2 and j == n//2):
        return

    if check_t[idx%4] == 'j' and j == (n-1) - turn:
        idx += 1 # 방향 바꾸기
        turn += 1
    elif check_t[idx%4] == 'i' and i == (n-1) - turn:
        idx += 1
        turn += 1
    elif check_t[idx%4] == '-j' and j == turn:
        idx += 1
        turn += 1
    elif check_t[idx%4] == '-i' and i == turn:
        idx += 1
        turn += 1
    ti,tj = order_t[idx%4] #direction
    ni,nj = i+ti, j+tj
    search_true(gmap,[ni,nj],idx,n,cnt+1, turn)

order_f= [[1,0],[0,1],[-1,0],[0,-1]]
check_f = ['i','j','-i','-j']

def search_false(gmap, curr, idx, n, cnt, turn):
    i, j = curr
    gmap[i][j] = cnt

    if n%2==0 and (n//2-1 <= i <= n//2 and n//2 -1 <= j <= n//2):
        return
    if n % 2 != 0 and (i == n//2 and j == n//2):
        return

    if check_f[idx%4] == 'j' and j == (n-1) - turn:
        idx += 1 # 방향 바꾸기
        turn += 1
    elif check_f[idx%4] == 'i' and i == (n-1) - turn:
        idx += 1
        turn += 1
    elif check_f[idx%4] == '-j' and j == turn:
        idx += 1
        turn += 1
    elif check_f[idx%4] == '-i' and i == turn:
        idx += 1
        turn += 1
    ti,tj = order_f[idx%4] #direction
    ni,nj = i+ti, j+tj
    search_false(gmap,[ni,nj],idx,n,cnt+1, turn)

def solution(n, clockwise):
    gmap = [[0 for _ in range(n)] for _ in range(n)]
    start_point_t = [[0, 0], [0, n - 1], [n - 1, n - 1], [n - 1, 0]]
    start_point_f = [[0, 0], [n - 1, 0], [n - 1, n - 1], [0, n - 1]]
    # 시계 방향
    if clockwise:
        for idx in range(len(start_point_t)):
            search_true(gmap, start_point_t[idx], idx, n, 1, 1)
    else:
        for idx in range(len(start_point_f)):
            search_false(gmap, start_point_f[idx], idx, n, 1, 1)

    return gmap
