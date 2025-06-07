# 라면 공장 재고
## 목표: ❗ "라면이 떨어지지 않게 하면서 최소한의 횟수로 외국에서 받아오는 것"
import heapq # 우선순위 큐: 받을 수 있는 라면 중에서 가장 많은 양부터 꺼낼 수 있게”

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30

def get_minimum_number_of_days_to_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = [] # 우선순위 큐를 사용하여 공급량을 관리

    while stock < k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock: # 현재 재고로 공급받을 수 있는 날짜인 경우
            heapq.heappush(max_heap, -supplies[last_added_date_index])  # 공급량을 음수로 저장하여 최대 힙으로 사용
            last_added_date_index += 1 # 다음 날짜로 이동

        answer += 1
        heappop = heapq.heappop(max_heap) # 최대 공급량을 꺼냄
        stock += -heappop
    return answer