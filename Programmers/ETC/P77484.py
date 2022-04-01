# 2021 Dev_Matching P77484 로또의 최고 순위와 최저 순위
"""
set을 통해 교집합을 찾아낸 후 이를 기준으로 lowest와 highest를 측정
"""
def solution(lottos, win_nums):
    result = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    lot = set(lottos)
    win = set(win_nums)

    same = len(lot & win)
    lowest = result[same]
    highest = result[same + lottos.count(0)]
    return [highest, lowest]
