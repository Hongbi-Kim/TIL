#######################################################################################################################
# 2018 KAKAO BLIND RECRUITMENT → [1차] 캐시 
#######################################################################################################################

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)        # 이전 위치 제거
            cache.append(city)        # 가장 최근에 사용된 것으로 갱신
            answer += 1               # cache hit
        else:
            answer += 5               # cache miss
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.popleft()   # 가장 오래된 것 제거
                cache.append(city)    # 새로운 도시 추가

    return answer


from collections import OrderedDict

def solution(cacheSize, cities):
    cache = OrderedDict()
    total_time = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            # ✅ Cache Hit
            total_time += 1
            cache.move_to_end(city)  # 최근 사용으로 갱신
        else:
            # ❌ Cache Miss
            total_time += 5
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.popitem(last=False)  # 가장 오래된 항목 제거
                cache[city] = True  # 새 항목 추가
    return total_time
