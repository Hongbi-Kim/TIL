#######################################################################################################################
# 2022 KAKAO BLIND RECRUITMENT → 양궁대회
#######################################################################################################################
# DFS + 백트래킹 최적화 문제
# 라이언이 최대 점수 차로 이겨야 함.
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

def solution(n, info):
    answer = []
    max_diff = 0  # 최대 점수차 저장

    def dfs(index, remain, ryan): # 지금 처리 중인 점수(0이면 10점, 10이면 0점), 남은 화살 수, 라이언이 쏜 화살을 저장하는 리스트
        nonlocal answer, max_diff # 전역 변수 사용

        if index == 11:  # 0점까지 다 처리했으면
            if remain > 0:
                ryan[10] += remain  # 남은 화살은 0점에 몰빵 → 0점을 맞춰도 아무도 점수를 얻지 못하므로 상관없음

            # 점수 계산
            apeach_score, ryan_score = 0, 0
            for i in range(11):
                if info[i] == 0 and ryan[i] == 0: # 어피치도, 라이언도 그 점수에 안 쐈으면 → 그냥 넘어감
                    continue
                if ryan[i] > info[i]: # 라이언이 더 많이 쐈을 경우
                    ryan_score += (10 - i)
                else:
                    apeach_score += (10 - i)

            diff = ryan_score - apeach_score

            if diff > 0: # 라이언이 이긴 경우에만 저장
                if diff > max_diff: # 점수차가 더 크면 바로 저장
                    max_diff = diff
                    answer = ryan[:]
                elif diff == max_diff:
                    # 제한사항: 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
                    # 동점일 때는 0점부터 비교해서 더 많이 쏜 경우 선택해요!
                    for i in range(10, -1, -1):
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
                        elif ryan[i] < answer[i]:
                            break
            if remain > 0:
                ryan[10] -= remain  # ryan[10]에 몰빵했던 남은 화살을 다시 빼줍니다.
            return

        # 라이언이 이 점수 이기려면: 어피치보다 1발 더 쏘기
        if remain > info[index]:
            ryan[index] = info[index] + 1
            dfs(index + 1, remain - ryan[index], ryan)
            ryan[index] = 0  # 백트래킹, 없었던걸로 돌아가서 점수를 포기한 경우도 계산하자!

        # 이 점수 포기
        dfs(index + 1, remain, ryan)

    dfs(0, n, [0]*11)

    return answer if answer else [-1]

#######################################################################################################################
# 안전 영역 (https://www.acmicpc.net/problem/2468)
#######################################################################################################################
# 백준 버전
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

from collections import deque

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

n = 5
area = [[6,8,2,6,2],[3,2,3,4,6],[6,7,3,3,2],[7,2,5,3,6],[8,9,5,2,7]]

max_height = max(max(row) for row in area)
max_safe_zone = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, rain, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:  # 격자 밖이면 못 감(경계에 막힘)
                if not visited[nx][ny] and area[nx][ny] > rain: # 이미 방문한 곳은 다시 안 감(중복 막음), # 잠긴 칸(<=rain)은 못 감(물에 막힘)
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for rain in range(max_height + 1):  # 비의 높이 0부터 최대 높이까지
    visited = [[False]*N for _ in range(N)]
    safe_zone_count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > rain:
                bfs(i, j, rain, visited)
                safe_zone_count += 1

    max_safe_zone = max(max_safe_zone, safe_zone_count)

print(max_safe_zone)


# 프로그래머스 input 형 

n = 5
areas = [[6,8,2,6,2],[3,2,3,4,6],[6,7,3,3,2],[7,2,5,3,6],[8,9,5,2,7]]