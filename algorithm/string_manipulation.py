#######################################################################################################################
# 카카오 신입 개발자 블라인드 채용 1차 코딩테스트: 문자열 압축
#######################################################################################################################

# time error
def solution(s):
    n = len(s)
    compression_length_array = []
    
    for split_size in range(1, n // 2 + 1):
        compressed = ""
        splited = [s[i:i+split_size] for i in range(0, n, split_size)] # 문자열 슬라이싱으로 전체 리스트 생성 → O(N) 공간
        count = 1
        
        for j in range(0, len(splited) - 1):
            cur, next = splited[j], splited[j+1]
            if cur == next:
                count += 1
            else:
                if count > 1:
                    compressed += (str(count) + cur)
                else:
                    compressed += cur
                count = 1
        if count > 1:
            compressed += (str(count) + splited[-1]) # 문자열 누적은 O(N²) 시간 → 새 문자열 계속 생성됨
        else:
            compressed += splited[-1]
        compression_length_array.append(len(compressed))
        
    return min(compression_length_array)

# 최적화된 코드
def solution(s):
    n = len(s)
    if n == 1:
        return 1

    min_length = n  # 압축 전 길이로 초기화

    for size in range(1, n // 2 + 1):
        compressed = []
        prev = s[0:size]
        count = 1

        for i in range(size, n, size):
            cur = s[i:i+size]
            if cur == prev:
                count += 1
            else:
                if count > 1:
                    compressed.append(str(count))
                compressed.append(prev)
                prev = cur
                count = 1

        if count > 1:
            compressed.append(str(count))
        compressed.append(prev)

        compressed_len = sum(len(chunk) for chunk in compressed)
        min_length = min(min_length, compressed_len)
        
    return min_length


#######################################################################################################################
# 카카오 신입 개발자 블라인드 채용 1차 코딩테스트: 올바른 괄호 문자열 만들기
#######################################################################################################################

from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string): # 올바른 괄호 문자열인지 확인하는 함수 -> () 짝도 맞아야 하고, ()가 올바른 순서로 열리고 닫혀야 함
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

def separate_to_u_v(string): # 균형잡힌 문자열을 u와 v로 분리하는 함수
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break
    
    v = "".join(queue)
    return u, v


def reverse_parentheses(string):  # 뒤집기
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string

def change_to_correct_parentheses(string): # 균형잡힌 문자열을 올바른 괄호 문자열로 바꾸는 함수
    if string == '':  
        return ''
    u, v = separate_to_u_v(string)
    if is_correct_parentheses(u):  
        return u + change_to_correct_parentheses(v) # u가 올바른 괄호 문자열인 경우
    else: 
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)

# 방법2
# 큐 사용하지 않고 문자열 슬라이싱으로 구현
def is_correct_parentheses(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

def separate_to_u_v(s):
    left = right = 0
    for i, ch in enumerate(s):
        if ch == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return s[:i+1], s[i+1:]

def reverse_parentheses(s):
    return ''.join('(' if ch == ')' else ')' for ch in s)

def change_to_correct_parentheses(s):
    if not s:
        return ''
    u, v = separate_to_u_v(s)
    if is_correct_parentheses(u):
        return u + change_to_correct_parentheses(v)
    else:
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])

def get_correct_parentheses(s):
    return s if is_correct_parentheses(s) else change_to_correct_parentheses(s)


#######################################################################################################################
# 2018 KAKAO BLIND RECRUITMENT: [3차] 방금그곡 https://school.programmers.co.kr/learn/courses/30/lessons/17683
#######################################################################################################################

import time
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def convert_sharp_notes(notes):
    return notes.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f') \
                .replace('G#', 'g').replace('A#', 'a')

def get_minutes(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    return (eh * 60 + em) - (sh * 60 + sm)

def solution(m, musicinfos):
    m = convert_sharp_notes(m)
    matched_song = ('(None)', 0)  # (제목, 재생시간)

    for info in musicinfos:
        start, end, title, sheet = info.split(',')
        duration = get_minutes(start, end)
        sheet = convert_sharp_notes(sheet)

        full_played = (sheet * (duration // len(sheet))) + sheet[:duration % len(sheet)]

        if m in full_played:
            if duration > matched_song[1]: # 조건이 일치하는 경우, 재생시간이 긴 곡을 반환
                matched_song = (title, duration)

    return matched_song[0]

#######################################################################################################################
# 2022 KAKAO BLIND RECRUITMENT: k진수에서 소수 개수 구하기 (https://school.programmers.co.kr/learn/courses/30/lessons/92335)
#######################################################################################################################
n = 437674
k = 3

# k진수는 숫자를 k개의 숫자(기호)를 사용해 표현하는 방식
def to_k_base(n, k):
    result = ''
    while n > 0:
        result = str(n % k) + result
        n //= k
    return result

# 소수는 1과 자기 자신만을 약수로 가지는 자연수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # √n까지만 확인
        if n % i == 0:
            return False
    return True

def solution(n, k):
    k_base = to_k_base(n, k)
    parts = k_base.split('0')
    
    result = 0
    for p in parts:
        if p == '':
            continue
        if is_prime(int(p)):
            result += 1
    return result

#######################################################################################################################
# 2023 KAKAO BLIND RECRUITMENT: 개인전보 수집 유효기간
#######################################################################################################################
today = "2022.05.19"
terms= ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def date_to_days(date):
    y, m, d = map(int, date.split("."))
    return y*12*28+m*28+d

def solution(today, terms, privacies):
    term_dict = {}
    for term in terms:
        tm_type, tm_m = term.split(" ")
        term_dict[tm_type] = tm_m

    answer = []
    today_days = date_to_days(today)
    for i, privacy in enumerate(privacies):
        start_days = date_to_days(privacy.split(" ")[0])
        type = privacy.split(" ")[1]
        expiry_days = start_days + int(term_dict[type])*28

        if expiry_days <= today_days:
            answer.append(i + 1)

    return answer

# 28일로 고정되어있지 않을 때
from datetime import datetime
from dateutil.relativedelta import relativedelta  # pip install python-dateutil

today = datetime.strptime(today, "%Y.%m.%d") # datetime.datetime(2022, 5, 19, 0, 0)
dt = datetime.strptime("2022.05.19 13:45", "%Y.%m.%d %H:%M") # datetime.datetime(2022, 5, 19, 13, 45)
print("연:", dt.year)    # 2022
print("월:", dt.month)   # 5
print("일:", dt.day)     # 19
print("시:", dt.hour)    # 13
print("분:", dt.minute)  # 45
print("초:", dt.second)  # 0 (초를 넣지 않았기 때문에 기본값 0)

term_dict = {t.split()[0]: int(t.split()[1]) for t in terms} # {'A': 6, 'B': 12, 'C': 3}
result = []

for i, p in enumerate(privacies):
    date_str, term_type = p.split()
    collected = datetime.strptime(date_str, "%Y.%m.%d")
    expire_date = collected + relativedelta(months=term_dict[term_type])
    
    # 당일 포함 X → 유효기간의 하루 전까지 보관 가능
    if expire_date <= today:
        result.append(i + 1)


#######################################################################################################################
# 2018 KAKAO BLIND RECRUITMENT: [1차] 다트게임
#######################################################################################################################

dartResult = "1S2D*3T"

scores = []
i = 0
length = len(dartResult)

while i < length:
    # 10인 경우를 따로 처리
    if dartResult[i] == "1" and i+1 < length and dartResult[i+1] == "0":
        score = 10
        i += 2
    else:
        score = int(dartResult[i])
        i += 1

    # 보너스
    bonus = dartResult[i]
    if bonus == "S":
        score = score ** 1
    elif bonus == "D":
        score = score ** 2
    else: # bonus == "T"
        score = score ** 3
    i += 1

    # 옵션
    if i < length and dartResult[i] in "*#":
        if dartResult[i] == "*":
            score *= 2
            if scores:
                scores[-1] *= 2
        else:
            score *= -1
        i += 1

    scores.append(score)
sum(scores)     


#######################################################################################################################
# 2018 KAKAO BLIND RECRUITMENT: 비밀지도
#######################################################################################################################

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

format(9, "b")

answer = []
for i in range(n):
    # 비트 OR 연산
    combined = arr1[i] | arr2[i]
    # 이진수로 변환, n자리로 맞추기
    binary_str = format(combined, 'b').zfill(n)
    # '#'과 ' '로 변환
    line = ''.join(['#' if c == '1' else ' ' for c in binary_str])
    answer.append(line)

#######################################################################################################################
# 2018 KAKAO BLIND RECRUITMENT: [3차] 파일명 정렬
#######################################################################################################################
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
    def split_file(index, file):
        head, number, i = '', '', 0
        length = len(file)

        while i < length and not file[i].isdigit():
            head += file[i]
            i += 1

        while i < length and file[i].isdigit():
            number += file[i]
            i += 1

        return (head.lower(), int(number), index, file)  # index 추가!


    # 튜플 정렬 → 정렬 기준은 head, number, index 순서
    # i = 0
    # f = files[0]
    for i, f in enumerate(files):
        files[i] = split_file(i, f)
        # files[i] = (files[i][0], files[i][1], i, files[i][3])  # index 추가
    sorted_files = sorted(files)
    
    # 결과에서 파일명만 추출
    return [x[3] for x in sorted_files]

from math import ceil
from collections import defaultdict
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

basic_time, basic_fee, unit_time, unit_fee = fees
in_record = dict()
total_time = defaultdict(int)

for record in records:
    timerecord, number, state = record.split()
    timerecord = int(timerecord.split(":")[0]) * 60 + int(timerecord.split(":")[1])

    if state == "IN":
        in_record[number] = timerecord
    else:
        in_time = in_record.pop(number)
        total_time[number] += timerecord - in_time

for number, in_time in in_record.items():
    total_time[number] += (23*60 + 59) - in_time

result = []
for number in sorted(total_time.keys()):
    t = total_time[number]
    if t <= basic_time:
        result.append(basic_fee)
    else:
        extra_time = ceil((t - basic_time) / unit_time)
        result.append(basic_fee + extra_time * unit_fee)

#######################################################################################################################
# 1920: 수 찾기
#######################################################################################################################

import sys

input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)

N, K = map(int, input().split())
lines = list(map(int, input().split()))
N = 4
K = 11
lines = [802, 743, 457, 539]

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lines = list(map(int, input().split()))
max_length = sorted(lines)[0]

ctx = 0
while ctx < K:
    ctx = 0
    for line in lines:
        ctx += line // max_length
    if K // ctx > 1:
        max_length = max_length // (K // ctx)
    elif K // ctx == 1 and not ctx >= K:
        max_length -= 1

from itertools import combinations
list(combinations([1,2,3,4],2))
list(combinations(A,2))

A = "ACAYKP"
B = "CAPCAK"

# 입력
A = input().strip()
B = input().strip()

# DP 테이블 초기화
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

# DP 진행
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 출력
print(dp[len(A)][len(B)])


#######################################################################################################################
# 방금그곡
#######################################################################################################################
m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def solution(m, musicinfos):
    def parse_melody(melody):
        """멜로디를 개별 음표로 파싱"""
        notes = []
        i = 0
        while i < len(melody):
            if i + 1 < len(melody) and melody[i + 1] == '#':
                notes.append(melody[i:i+2])
                i += 2
            else:
                notes.append(melody[i])
                i += 1
        return notes
    
    def time_to_minutes(time_str):
        """시간을 분 단위로 변환"""
        h, m = map(int, time_str.split(':'))
        return h * 60 + m
    
    def expand_melody(sheet, play_time):
        """악보를 재생 시간만큼 확장"""
        notes = parse_melody(sheet)
        if not notes or play_time <= 0:
            return []
        
        result = []
        for i in range(play_time):
            result.append(notes[i % len(notes)])
        return result
    
    def contains_melody(played_notes, target_notes):
        """played_notes에 target_notes가 포함되어 있는지 확인"""
        if len(target_notes) == 0:
            return True
        if len(played_notes) < len(target_notes):
            return False
        
        # 슬라이딩 윈도우로 비교
        for i in range(len(played_notes) - len(target_notes) + 1):
            if played_notes[i:i+len(target_notes)] == target_notes:
                return True
        return False
    
    target_notes = parse_melody(m)
    best_duration = -1
    best_title = "(None)"
    
    for info in musicinfos:
        start_time, end_time, title, sheet = info.split(',')
        
        # 재생 시간 계산
        start_minutes = time_to_minutes(start_time)
        end_minutes = time_to_minutes(end_time)
        
        duration = end_minutes - start_minutes
        
        # 실제 재생된 멜로디 생성
        played_notes = expand_melody(sheet, duration)
        
        # 멜로디 포함 여부 확인
        if contains_melody(played_notes, target_notes):
            # 더 긴 재생 시간이면 업데이트
            if duration > best_duration:
                best_duration = duration
                best_title = title
    
    return best_title


#######################################################################################################################
# 가장큰수
#######################################################################################################################

numbers = [6, 10, 2]
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

#######################################################################################################################
# 메뉴 리뉴얼
#######################################################################################################################


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
# ["AC", "ACDE", "BCFG", "CDE"]

from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    # c = 2
    # order = "ABCFG"
    for c in course:
        combs = []
        for order in orders:
            sorted_order = sorted(order)
            combs += combinations(sorted_order, c)
        
        count = Counter(combs)

        if count:
            max_cnt = max(count.values())
            if max_cnt >= 2:
                for comb in count:
                    if count[comb] == max_cnt:
                        result.append("".join(comb))

    return sorted(result)


#######################################################################################################################
# 소수 구하기 (https://www.acmicpc.net/problem/1929)
#######################################################################################################################
N, M = map(int, input().split())
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(N, M + 1):
    if is_prime(num):
        print(num)