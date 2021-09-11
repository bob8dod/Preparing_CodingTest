from collections import defaultdict

def solution(fees, records):
    answer = []
    time_answer = []
    car_dict = defaultdict(list)
    for r in records:
        time, car_num, _ = r.split()
        car_dict[car_num].append(time)
    for num in sorted(car_dict):
        time_list = car_dict[num]
        i = 0
        result_time = 0
        while i < len(time_list):
            in_time = int(time_list[i].split(':')[0])*60 + int(time_list[i].split(':')[1])
            if i + 1 >= len(time_list):
                out_time = 23 * 60 + 59
            else:
                out_time = int(time_list[i+1].split(':')[0])*60 + int(time_list[i+1].split(':')[1])
            result_time = result_time + out_time - in_time

            i += 2

        time_answer.append(result_time)

    for t in time_answer:
        base_time, base_fee, add_time, add_fee = fees
        if t < base_time:
            answer.append(base_fee)
        else:
            if (t - base_time) % add_time == 0:
                added_fee = (t - base_time)//add_time
            else:
                added_fee = (t - base_time)//add_time + 1
            answer.append(base_fee + added_fee * add_fee)
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
