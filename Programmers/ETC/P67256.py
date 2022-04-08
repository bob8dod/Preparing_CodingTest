# 프로그래머스 2020 카카오 인턴십 구현 P67256 키패드 누르기 
"""
핵심은 * 0 # -> 10 11 12 로 변경하여 
숫자로써 판단한 부분
"""

def getCnt(curr, n, dir):
    cnt = 0
    if curr < n:
        while True:
            if curr == n:
                return cnt
            if curr + dir == n:
                return cnt + 1
            curr += 3
            cnt += 1
    else:
        while True:
            if curr == n:
                return cnt
            if curr + dir == n:
                return cnt + 1
            curr -= 3
            cnt += 1


def solution(numbers, hand):

    nums = []
    for i in numbers:
        if i == 0: nums.append(11)
        else: nums.append(i)

    le = {1, 4, 7}
    ri = {3, 6, 9}
    mid = {2, 5, 8, 11}

    curr_l, curr_r = 10, 12

    answer = ''
    for n in nums:
        if n in le:
            curr_l = n
            answer += 'L'
        if n in ri:
            curr_r = n
            answer += 'R'
        if n in mid:
            left = getCnt(curr_l, n, 1)
            right = getCnt(curr_r, n, -1)
            if left < right:
                curr_l = n
                answer += 'L'
            elif right < left:
                curr_r = n
                answer += 'R'
            else:
                if hand == 'left':
                    curr_l = n
                    answer += 'L'
                else:
                    curr_r = n
                    answer += 'R'

    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
