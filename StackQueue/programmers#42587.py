from collections import deque

def solution(priorities, location):
    max_check = deque(sorted(priorities, reverse=True))
    answer_arr = deque([[v,i] for i,v in enumerate(priorities)])
    turn = 1
    while answer_arr:
        if answer_arr[0][0] == max_check[0]:
            check = answer_arr.popleft()
            max_check.popleft()
            if check[1] == location:
                return turn
            turn += 1
        else:
            answer_arr.append(answer_arr.popleft())
