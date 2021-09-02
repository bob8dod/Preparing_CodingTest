from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        # 입력받은 문자열을 한 문자씩 리스트로 변형, map과 ''.join을 사용하여 permutations의 결과의 문자들을 다시 문자열로 병합 후 int형으로 다시 변환, 그 후 집합a에 or 연산을 통해 더해줌
        a |= set(map(int, map("".join, permutations(list(n), i + 1)))) 
    a -= set(range(0, 2)) # 0,1 제거 (소수 판단 시 제외해주기 위함)
    for i in range(2, int(max(a) ** 0.5) + 1): # 가장 큰수의 제곱근까지의 범위로 설정함으로써 시간복잡도 Down
        a -= set(range(i * 2, max(a) + 1, i))  # 소수가 아닌 수들을 기존 집합a에서 제거해줌
    return len(a) # 결과
