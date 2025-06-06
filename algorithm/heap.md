### Heap
- 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
- O(log(N))
- 사용하는 경우
    - 데이터를 넣을 때마다 최댓값을 동적으로 변경시키며
    - 최솟/최댓값을 바로 꺼낼 수 있는 

```
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

print(heap)  # [1, 3, 7, 4]

heapq.heappop(heap) # 최솟값 빼기
```
- 이진 트리 구조 시각화

        1
       / \
      3   7
     /
    4
