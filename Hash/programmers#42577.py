def solution(phone_book): 
    answer = True
    hash_map = {} # 해당 요소가 존재하는지 탐색할 때, dict를 사용하여 시간복잡도에서 유리
    # 모든 전화번호를 dict에 저장
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    # 각 전화번호에 대해서 탐색
    for phone_number in phone_book:
        temp = "" # 접두어인 경우를 탐색하기 위한 문자열 저장
        # 해당 전화번호를 앞에서 부터 한글자씩 temp에 저장
        for number in phone_number:
            temp += number
            # 해당 전화번호의 앞부분의 일부를 저장한 temp와 동일한 전화번호가 있는지 판단
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
