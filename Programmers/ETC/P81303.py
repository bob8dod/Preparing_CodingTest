# 2021 카카오 체용연계형 인턴십 표 편집 P81303
"""
시도: 리스트로 구현, 삭제 노드를 0으로 표시, 존재하는 노드는 1로 표시,
      0이 나올 경우 while을 통해 넘어가는 형식으로 구현 -> 정확도, 효율성 둘다 실패
풀이: 링크드 리스트를 통해 구현.
     삭제, 복구 시 문제에 나온 조건에 따라 링크드리스트 초기화, 포인트 이동이 핵심
"""

def solution(n, k, cmd):
    table = {i:[i-1,i+1] for i in range(n)} # 링크드 리스트 딕셔너리로 구현
    table[0] = [None,1] # 가장 처음 노드
    table[n-1] = [n-2,None] # 마지막 노드

    answer = ['O' for _ in range(n)]
    curr = k
    stk = [] # 복구를 위한 stack 구조

    for c in cmd:
        # 삭제
        if c == 'C':
            prev, next_ = table[curr]
            stk.append([prev,curr,next_])
            answer[curr] = 'X'

            # 삭제 시 링크드 리스트 초기화
            if prev is None:
                table[next_][0] = None
            elif next_ is None:
                table[prev][1] = None
            else:
                table[prev][1] = next_
                table[next_][0] = prev

            # 삭제 후 포인트 이동
            if next_ is None:
                curr = prev
            else:
                curr = next_

        # 복구
        elif c == 'Z':
            prev, now, next_ = stk.pop()
            answer[now] = 'O'

            # 복구 시 링크드 리스트 초기화
            if prev is None:
                table[next_][0] = now
            elif next_ is None:
                table[prev][1] = now
            else:
                table[prev][1] = now
                table[next_][0] = now

        # 포인트 이동
        else:
            di, step = c.split()
            step = int(step)
            if di == 'D':
                for _ in range(step):
                    curr = table[curr][1]
            else:
                for _ in range(step):
                    curr = table[curr][0]

    return ''.join(answer)
