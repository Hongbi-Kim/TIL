# 코딩테스트 준비하기
<br>

## [기술블로그🐕](https://ai-rain.tistory.com/category/Algorithm)
<br>


## 미리 알아두면 좋은 함수/방법
- 소수 판별
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```
<br>


- K 진수 구하기
```
# K진수 구하기
def to_k_base(n, k):
    result = ""
    while n > 0:
        result = str(n%k) + result
        n //= k
    return result
to_k_base(11,2)
```
```
print(format(11,'b')) # 2진수 1011
print(format(11,'o')) # 8진수 13
print(format(11,'x')) # 16진수 b
```

<br>

```
from collections import OrderedDict

cache = OrderedDict()
cache["a"] = True
cache["b"] = True
print(cache)
cache.move_to_end("a") # 맨 뒤로
print(cache)
cache.popitem(last=False) # 맨 앞 제거
cache
```
```
OrderedDict([('a', True), ('b', True)])
OrderedDict([('b', True), ('a', True)])
OrderedDict([('a', True)])
```


<!-- ## 프로그래머스
|문제명|유형|난이도|
|:-:|:-:|:-:|
|서울에서 김서방 찾기|구현 (Implementation), 리스트 탐색|1|
|[거리두기 확인하기](https://school.programmers.co.kr/learn/courses/30/lessons/81302#fn1)|BFS, 2차원|2|
|[방금그곡](https://school.programmers.co.kr/learn/courses/30/lessons/17683)|string, simulation|2|
|[캐시](https://school.programmers.co.kr/learn/courses/30/lessons/17680)|자료구조, 시뮬레이션, 문자열|2|
|[k진수에서 소수 개수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/92335)|문자열|2|
|다트게임|문자열, 소수 구하기|1| -->