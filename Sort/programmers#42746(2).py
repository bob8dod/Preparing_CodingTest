def solution(numbers):
    numbers = list(map(str, numbers)) # 문자열로써 비교하기 위해
    # 가장 긴 수의 길이가 최대 3이므로 (1000보다 클 수 없음) 비교를 위해 해당 수를 3번 복사해주고 문자열로써 비교하여 정렬
    numbers.sort(key=lambda x: x*3, reverse=True) 
    return str(int(''.join(numbers))) #정렬 결과를 반환
