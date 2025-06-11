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


