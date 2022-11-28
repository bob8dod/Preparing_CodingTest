from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    
    answer = 0
    cache_space = deque([])
    for city in cities:
        l_city = city.lower()
        if l_city in cache_space:
            cache_space.remove(l_city)
            answer += 1
        else:
            if len(cache_space) >= cacheSize:
                cache_space.popleft()
            answer += 5
        cache_space.append(l_city)
    return answer
        
