# not using 
from collections import defaultdict, deque
def solution(operations):
    answer = []
    num_dict = defaultdict(int)
    queue = deque()
    for o in operations:
        if o[0] == 'I':
            queue.append(int(o[2:]))
            queue = deque(sorted(queue))
        elif queue and o == 'D 1':          
            queue.pop()
        elif queue and o == 'D -1':
            queue.popleft()

    if not queue:
        answer = [0,0]
    else:
        answer = [queue[-1],queue[0]]

    return answer
