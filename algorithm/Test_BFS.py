# 샤오미 로봇 청소기 
from collections import deque

r, c, d = 7, 4, 0
room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0] # 북, 동, 남, 서
dc = [0, 1, 0, -1] # 북, 동, 남, 서


# 방향 전환
def get_d_index_when_rotate_to_left(d): # 현재 방향에서 왼쪽으로 회전
    return (d + 3) % 4

# 후진
def get_d_index_when_go_back(d): # 현재 방향에서 후진
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleand = 1 # 청소하는 칸의 개수
    room_map[r][c] = 2 # 청소한 칸은 2로 표시
    queue = deque([[r, c, d]]) # 현재 위치와 방향을 큐에 저장


    while queue:
        r, c, d = queue.popleft() # 현재 위치와 방향을 꺼냄
        temp_d = d

        for i in range(4): # 현재 방향을 기준으로 왼쪽 방향부터 탐색
            temp_d = get_d_index_when_rotate_to_left(temp_d) # 방향 전환
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 < new_r < n and 0 < new_c < m and room_map[new_r][new_c] == 0: # 청소하지 않은 칸인 경우
                count_of_departments_cleand += 1 # 청소한 칸의 개수 증가
                room_map[new_r][new_c] = 2 # 청소한 칸은 2로 표시
                queue.append([new_r, new_c, temp_d]) # 큐에 새로운 위치와 방향을 추가
                break

            elif i == 3: # 네 방향 모두 청소가 되어 있는 경우
                new_c, new_r = c + dc[get_d_index_when_go_back(d)], r + dr[get_d_index_when_go_back(d)] # 후진
                queue.append([new_r, new_c, d]) # 큐에 후진한 위치와 방향을 추가

                if room_map[new_r][new_c] == 1: # 후진한 위치가 벽인 경우
                    return count_of_departments_cleand # 청소한 칸의 개수를 반환
                
