# 보드는 1차원 리스트로 구현한다.
game_board = [' ' for _ in range(9)]

# 비어 있는 칸을 찾아서 리스트로 반환한다.
def empty_cells(board):
    return [x for x, cell in enumerate(board) if cell == ' ']

# 비어 있는 칸에 둘 수 있는지 확인한다.
def valid_move(x):
    return x in empty_cells(game_board)

# 위치 x에 플레이어의 심볼을 놓는다.
def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

# 현재 게임 보드를 그린다.
def draw(board):
    for i, cell in enumerate(board):
        if i % 3 == 0:
            print("\n----------------")
        print(f'| {cell} ', end='')
    print("\n----------------")

# 보드의 상태를 평가한다.
def evaluate(board):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    else:
        return 0

# 승리 조건을 확인한다.
def check_win(board, player):
    win_conf = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conf

# 게임이 끝났는지 확인한다.
def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O') or ' ' not in board

# 미니맥스 알고리즘을 구현한다.
def minimax(board, depth, is_maximizing):
    if game_over(board) or depth == 0:
        return -1, evaluate(board)

    if is_maximizing:
        max_eval = float('-inf')
        best_move = -1
        for move in empty_cells(board):
            board[move] = 'X'
            eval = minimax(board, depth-1, False)[1]
            board[move] = ' '
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move, max_eval
    else:
        min_eval = float('inf')
        best_move = -1
        for move in empty_cells(board):
            board[move] = 'O'
            eval = minimax(board, depth-1, True)[1]
            board[move] = ' '
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return best_move, min_eval

# 메인 프로그램
player = 'X'
while True:
    draw(game_board)
    if game_over(game_board):
        break
    idx, _ = minimax(game_board, len(empty_cells(game_board)), player == 'X')
    move(idx, player)
    player = 'O' if player == 'X' else 'X'

if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')
