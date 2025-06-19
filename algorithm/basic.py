# k 진수 구하기
def to_k_base(n, k):
    result = ""
    while n > 0:
        result = (str(n % k)) + result
        n //= k
    return result

to_k_base(10, 2) # '1010'

# 약수 구하기
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # √n까지만 확인
        if n % i == 0:
            return False
    return True

is_prime(8)

# 시간
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
print(now)  # ex: 2025-06-19 11:32:00.123456

# 문자열 → 날짜 객체
date = datetime.strptime("2023.05.12", "%Y.%m.%d")
print(date.year, date.month, date.day)  # 2023 5 12

# 날짜 객체 → 문자열
formatted = date.strftime("%Y/%m/%d")
print(formatted)  # 2023/05/12


# 1달 뒤
new_date = date + relativedelta(months=1)
print(new_date)  # 2023-02-28

# 1년 2개월 10일 뒤
complex = date + relativedelta(years=1, months=2, days=10)
print(complex)  # 2024-04-10

# 6개월 전
past = date - relativedelta(months=6)
print(past)  # 2022-07-31