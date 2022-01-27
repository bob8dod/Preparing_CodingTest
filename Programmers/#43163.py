# 단어 변환 _ 60min
"""
이전에 풀었던 DFS 방식 (뿌리는 내리는 순간에 min을 측정, 각각의 노드를 memo로 저장하여 DP로 푸는)
과 유사하지만, 크게 차이가 나는 부분은 visited를 그 뿌리마다 넘겨주며 판단.
즉, 공통된 visited가 아닌 그 뿌리마다의 visited를 사용.
즉, 하나의 뿌리에서 word 중에 이미 visited 된 애들에 대해서는 serach하지 않고
또 word 중에 변경 가능한 애들로만 뿌리를 내림 (이때 +1)
뿌리를 내리는 애들 중에서 결과적으로 최솟값을 나타내는 하나를 선택.
그럼 결론적으로 begin에 해당하는 memo값이 결론값.
이 값이 maxsize보다 같거나 클 경우 원하는 target에 도달하지 못한다는 뜻이기에 0반환
"""
import sys

min_re = {}
def dfs(curr, target, words, visited):
    global result

    if curr in min_re:
        return min_re[curr]
    if curr == target:
        return 0

    visited[curr] = 1

    tem_li = []
    for word in words:
        if visited[word]:
            continue
        tem = 0
        for c1, c2 in zip(curr,word):
            if c1 != c2: tem+=1
        if tem == 1:
            tem_li.append(1 + dfs(word, target, words, visited))

    if len(tem_li) == 0:
        min_re[curr] = sys.maxsize
        return min_re[curr]

    min_re[curr] = min(tem_li)
    return min_re[curr]


def solution(begin, target, words):
    visited = {word:0 for word in words}
    dfs(begin, target, words, visited)
    return min_re[begin] if min_re[begin] < sys.maxsize else 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
