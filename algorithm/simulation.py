#######################################################################################################################
# 새로운 게임 2 https://www.acmicpc.net/problem/17837
#######################################################################################################################

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
# 0: 흰색, 1: 빨간색, 2: 파란색
start_horse_location_and_directions = [ # 행, 열, 이동방향
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]

# 동, 서, 북, 남
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 말은 순서대로 이동합니다 → 말의 순서에 따라 반복문
# 말이 쌓일 수 있습니다 → 맵에 말이 쌓이는 걸 저장해놔야 함.
# 쌓인 순서대로 이동함 → 스택을 써야겠구나!

def get_d_index_when_go_back(d):
    if d % 2 == 0:       # 방향이 0 (오른쪽) 또는 2 (위쪽) 이면
        return d + 1     # → 반대 방향으로 전환: 1 (왼쪽), 3 (아래쪽)
    else:                # 방향이 1 (왼쪽) 또는 3 (아래쪽) 이면
        return d - 1     # → 반대 방향으로 전환: 0 (오른쪽), 2 (위쪽)

def get_game_over_turn_count(k, chess_map, start_horse_location_and_directions):
    n = len(chess_map)
    turn_count = 1
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]
    
    for i in range(k):
        r, c, d = start_horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)

    while turn_count <=1000:
        for horse_index in range(k):
            r, c, d = start_horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]

            #  3) 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
            if not 0 <= new_r < n or not 0 <= new_c < n or chess_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)
                
                start_horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]
                # 3) 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
                if not 0 <= new_r < n or not 0 <= new_c < n or chess_map[new_r][new_c] == 2:
                    continue

            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                # 여기서 이동해야 하는 애들은 현재 옮기는 말 위의!!! 말들이다.
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break


            # 2) 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
            if chess_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                # horse_location_and_directions 에 이동한 말들의 위치를 업데이트한다.
                start_horse_location_and_directions[moving_horse_index][0], start_horse_location_and_directions[moving_horse_index][1] = new_r, new_c
                
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count

        turn_count += 1
    return -1

