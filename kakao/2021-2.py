def make_change(n, k):
    result = ''

    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)

    return result[::-1]

def is_Prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False

    return True

def solution(n, k):
    answer = 0
    to_check = make_change(n, k)
    check_list = to_check.split('0')
    for i in check_list:
        if i != '' and is_Prime(int(i)):
            answer += 1

    return answer

print(solution(110011,10))
