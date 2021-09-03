def solution(brown, yellow):
    answer = []
    add = (brown-4)//2
    mul = yellow
    for x in range(1,add):
        y = add-x
        if x*y == yellow:
            if x >= y:
                answer=[x+2,y+2]
    return answer
