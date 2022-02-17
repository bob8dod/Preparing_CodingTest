#12981 영어끝말잇기 _ 20m
"""
실수를 줄이자. 실수 때문에 한 10분 이상은 버린듯.
최대한 빠르게 풀자! 가 아나라 시간을 좀 쓰더라도 정확히 푼다로 접근합시다.
[풀이]
check을 통해서 기존에 나온 단어인지를 확인,
end_w 를 통해 이전 단어의 끝char를 저장 후 다음 word의 시작char를 비교
"""
def solution(n, words):
    answer = []
    check = {words[0]}
    end_w = words[0][-1]
    time = 1
    
    for i in range(1, len(words)):
        seq = (i % n) + 1
        if (i)%n == 0: time+=1

        # 탈락
        if words[i][0] != end_w or words[i] in check:
            answer.append(seq)
            answer.append(time)
            break

        end_w = words[i][-1]
        check.add(words[i])

    if len(answer) == 0:
        answer = [0, 0]

    return answer
