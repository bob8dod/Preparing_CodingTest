# 단지 번호 붙이기

h_map = []
house = []
d = [[1,0], [0,-1], [-1,0], [0,1]]
visited = []


def find(i,j):
    print(i,j,h_map[i][j])
    if visited[i][j] == 1 or h_map[i][j] == 0 or (i < 0 or i >= N) or (j < 0 or j >= N):
        return 0
    visited[i][j] = 1
    if h_map[i][j] == 1:
        for j in range(4):
            find(i + d[j][1], j + d[j][0])+1
        # return house.append(1 + find(i+d[0][1], j+d[0][0]))


def solution():
    global N
    N = int(input())
    for i in range(N):
        h_map.append(list(map(int,list(input()))))
        visited.append([0 for i in range(N)])
    find(0,1)
    print(len(house))
    for i in house: print(i)

solution()
