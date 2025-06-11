#######################################################################################################################
# 샤오미 로봇 청소기 
#######################################################################################################################
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
                
#######################################################################################################################
# 나 잡아 봐라 → LINE 인턴 채용 코딩테스트
#######################################################################################################################
# 1. 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000
# 2. 브라운은 범위를 벗어나는 위치로 이동 불가, 코니가 범위를 벗어나면 게임이 끝남. 
from collections import deque
cony_loc = 11
brown_loc = 2

# case 1
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0)) # (위치, 시간)
    # visited[pos][t] = True → 브라운이 pos 위치에 t 시간에 도달한 적 있는지
    visited = [{} for _ in range(200001)] # visited[1] = { 1: True }


    while cony_loc <= 200000: # 코니의 위치가 범위를 벗어날 때까지 반복
        cony_loc += time # 코니는 현재 시간만큼 이동
        # 코니 위치에 현재 시간에 브라운도 도달했는지 확인
        if time in visited[cony_loc]:
            return time
        
        for i in range(0, len(queue)): # 브라운의 위치를 탐색
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_position = current_position - 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1    
            if new_position < 200001 and new_time not in visited[new_position]: 
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))


        time += 1


print(catch_me(11, 2))

cony = 11
brown = 2

# case 2
# 시간은 짝수/홀수만 구분하면 충분!
# 코니는 매 시간마다 앞으로 점점 더 멀어지고, (즉, t초일 때 cony 위치는 1개뿐)
# 브라운은 BFS로 "같은 시간에 같은 위치"만 체크하면 되기 때문에,시간이 홀수냐 짝수냐만 구분하면 충분합니다!
# 즉, 우리가 보장받고 싶은 건: 시간 t에 브라운이 pos에 도달한 적 있는가?
# visited[0][칸번호]: 짝수 초에 도착한 곳
# visited[1][칸번호]: 홀수 초에 도착한 곳

def catch_me(cony, brown):
    MAX = 200000
    visited = [[False] * (MAX + 1) for _ in range(2)]  # visited[time % 2][position]
    queue = deque()
    queue.append((brown, 0))
    visited[0][brown] = True

    time = 0
    while cony <= MAX:
        if visited[time % 2][cony]:  # 브라운이 같은 시간에 해당 위치에 있었다면 잡음
            return time

        time += 1
        cony += time  # 코니는 매초마다 time만큼 앞으로 점점 더 멀리 감

        for _ in range(len(queue)):  # 현재 시간에 브라운이 방문한 위치들만 처리
            pos, t = queue.popleft()
            for next_pos in [pos - 1, pos + 1, pos * 2]:
                if 0 <= next_pos <= MAX and not visited[time % 2][next_pos]:
                    visited[time % 2][next_pos] = True
                    queue.append((next_pos, time))

