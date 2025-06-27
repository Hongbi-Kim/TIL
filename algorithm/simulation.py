#######################################################################################################################
# 새로운 게임 2 https://www.acmicpc.net/problem/17837
#######################################################################################################################
# "시간의 흐름에 따라 규칙을 구현하는 방식" →  시뮬레이션
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

#######################################################################################################################
# 삼성 역량 테스트 - 2 구슬 탈출 https://www.acmicpc.net/problem/13460
#######################################################################################################################
from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]


def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0  # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()  # FIFO
        if try_count > 10:  # 10 이하여야 한다.
            break

        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O':  # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if game_map[next_red_row][next_red_col] == 'O':  # 빨간 구슬이 구멍에 떨어진다면(성공)
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count:  # 두 구슬이 같은 위치에 멈춘 경우 더 멀리 이동한 구슬이 뒤에서 온 것이므로 한 칸 뒤로
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False


m=4	
n=5	
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]


# 틀린 버전
def solution(m, n, board):
    visited = []
    length = 1
    answer = 0
    while length > 0:
        for i in range(m-1): # 높이
            for j in range(n-1): # 폭
                if (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]) and board[i][j] != "X":
                    visited.append((i,j))
                    visited.append((i,j+1))
                    visited.append((i+1,j))
                    visited.append((i+1, j+1))
        visited = list(set(visited))
        length = len(visited)
        answer += length
        for tup in visited:
            x, y = tup
            if x != m-1:
                temp = list(board[x+1])   
                temp[y] = board[x][y]         
                board[x] = ''.join(temp)
        temp = list(board[x])   
        temp[y] = 'X'         
        board[x] = ''.join(temp)
    return answer

  

def solution(m, n, board):
    # 1. 문자열 배열을 리스트의 리스트로 변환
    board = [list(row) for row in board]
    total_removed = 0

    while True:
        # 2. 지워질 위치 찾기
        to_remove = set()
        for i in range(m - 1):
            for j in range(n - 1):
                block = board[i][j]
                if block == "0":
                    continue
                if block == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    to_remove |= {(i, j), (i+1, j), (i, j+1), (i+1, j+1)} # 집합을 사용하여 중복 제거

        # 3. 더 이상 지울 게 없으면 종료
        if not to_remove:
            break

        # 4. 블록 지우기
        for i, j in to_remove:
            board[i][j] = "0"
        total_removed += len(to_remove)

        # 5. 블록 떨어뜨리기
        for j in range(n):  # 열 단위
            empty = []
            for i in range(m-1, -1, -1):  # 아래에서 위로
                if board[i][j] == "0":
                    empty.append(i)
                elif empty:
                    empty_i = empty.pop(0)
                    board[empty_i][j], board[i][j] = board[i][j], "0"
                    empty.append(i)

    return total_removed
