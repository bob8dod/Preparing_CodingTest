from collections import deque

def solution(bridge_length, weight, truck_weights):
    check_finished = truck_weights # 종료조건에서 사용하기 위한 초기의 대기 트럭들
    on_bridge = deque() # 다리를 건너고 있는 트럭들을 저장하기 위한 queue
    passed = [] # 다리를 건넌 트럭들을 저장하기 위한 list, 추후에 check_finished와 비교 (종료조건)
    truck_weights = deque(truck_weights) #대기 트럭들 또한 queue로 설정
    total_weight = 0 # 다리의 최대 수용 무게와 비교하기 위한 현재 다리위의 트럭들의 무게 합
    time = 1 # 시간측정
    while True:
    	#초기의 대기 트럭들과 다리를 건넌 트럭들이 같다면 종료
        if passed == check_finished: 
            break
            
        # 대기 트럭이 존재한다면 (대기트럭이 존재하지 않는데 시간측정될 때가 있음)
        if truck_weights: 
            next_truck = truck_weights[0] # 현재 시간에 들어와야 하는 순서의 트럭
            # 다리의 트럭 최대 수용 개수와 무게를 넘지 않는다면
            if len(on_bridge) < bridge_length and total_weight + next_truck <= weight:
                total_weight += next_truck # 무게의 합을 더해주고
                on_bridge.append([truck_weights.popleft(), time])
                # -> 현재 들어와야하는 트럭을 대기 트럭에서 빼고 추후의 시간을 비교 하기 위해
                # 들어왔을 때의 시점과 함께 다리를 건너고 있는 트럭의 queue에 저장
        time += 1 # 시간 측정 +1
        # (현재 다리 위에 있는 트럭중 가장 앞에 있는 트럭이 다리를 다 건너는 시점)
        if time - on_bridge[0][1] == bridge_length: # -> '현재 시간 - 들어온 시점'이 다리의 길이와 동일할 때
            total_weight -= on_bridge[0][0] # 현재 다리 위의 트럭의 무게에서 빠지는 트럭의 무게를 빼줌
            passed.append(on_bridge.popleft()[0]) # 다리를 건넌 트럭의 queue에 저장

    return time
