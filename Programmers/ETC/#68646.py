# 프로그래머스 월간 코드 챌린지 시즌1 P68646 풍선 터트리기
"""
[핵심 개념]
결국 기준이 되는 풍선의 왼쪽과 오른쪽 중 적어도 한 방향에서 풍선에 적힌 숫자보다 작은게 없다면
 -- if left_min > curr or right_min > curr
해당 풍선은 터트릴 수 있음

[풀이]
하지만 위의 코드의 min을 기준의 왼,오를 잘라서 min()함수로 구하면 시간초과.
결국 왼족과 오른쪽을 구분해서 생각하고
둘 중 하나라도 조건에 부합하다면 인정하는 꼴로 가줘야 함.
# 중복은 set으로 제거.
"""
def solution(a):
    result = {a[0],a[-1]}

    # left
    left_min = a[0]
    for i in range(1,len(a)-1):
        if left_min > a[i]:
            left_min = a[i]
            result.add(a[i])

    # right
    right_min = a[-1]
    for i in range(len(a)-2,0,-1):
        if right_min > a[i]:
            right_min = a[i]
            result.add(a[i])

    return len(result)


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
