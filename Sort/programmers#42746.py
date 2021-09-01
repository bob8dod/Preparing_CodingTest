def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))  # 숫자를 복사하기 위해 str로 변경
    max_len = sorted(map(len, numbers))[-1]  # 가장 큰 수의 길이를 확인
    compares = []  # 수를 복사하고 인덱스와 함께 저장하기 위한 리스트
    for i in range(len(numbers)):
        num = str(numbers[i]) * 4  # 해당 숫자들을 복제함
        new_num = [i, int(num[:max_len])]  # 복제한 숫자의 길이를 max_len으로 맞추고
        compares.append(new_num)  # 인덱스와 함께 저장
    result = sorted(compares, key=lambda x: x[1], reverse=True)  # 복제한 숫자들 크기 비교

    for idx, _ in result:  # 정렬된 리스트의 인덱스값 가져옴
        answer += numbers[idx]  # 해당 인덱스에 맞는 숫자를 차례대로 붙여줌

    if answer[0] == '0':  # 0일 경우 '0000' 이런식으로 표현되므로
        return '0'  # '0'으로만 반환
    return answer  # 결과 반환
