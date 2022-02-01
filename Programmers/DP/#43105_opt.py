# 43105 정수 삼각형 BestCode
"""
같은 풀이 방법이지만,
따로 tri_map이라는 것을 만들지 않고
주어진 trianlge의 인덱스를 그대로 사용해서 푼 버전
# 결론 : 굳이 tri_map을 만들어서 판단할 필요가 없었다..
"""
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0: triangle[i][j]+= triangle[i-1][0]
            elif j==i: triangle[i][j] += triangle[i-1][-1]
            else: triangle[i][j] = max(triangle[i][j]+triangle[i-1][j-1], triangle[i][j]+triangle[i-1][j])
    return max(triangle[-1])
