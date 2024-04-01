import queue

class State:
    def __init__(self, board, goal, depth):
        self.board = board   # 현재의 보드 상태
        self.depth = depth   # 깊이
        self.goal = goal     # 목표 상태

    def get_new_board(self, i1, i2, depth):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, depth)

    def expand(self, depth):
        result = []
        i = self.board.index(0)   # 숫자 0(빈칸)의 위치를 찾는다.
        if i not in [0, 3, 6]:    # LEFT 연산
            result.append(self.get_new_board(i, i-1, depth))
        if i not in [0, 1, 2]:    # UP 연산
            result.append(self.get_new_board(i, i-3, depth))
        if i not in [2, 5, 8]:    # RIGHT 연산
            result.append(self.get_new_board(i, i+1, depth))
        if i not in [6, 7, 8]:    # DOWN 연산
            result.append(self.get_new_board(i, i+3, depth))
        return result

    def f(self):
        return self.h() + self.g()

    def h(self):
        score = 0
        for i in range(9):
            if self.board[i] != 0 and self.board[i] != self.goal[i]:
                score += 1
        return score

    def g(self):
        return self.depth

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return self.board != other.board

    def __lt__(self, other):
        return self.f() < other.f()

    def __gt__(self, other):
        return self.f() > other.f()

    def __str__(self):
        return f"f(n)={self.f()} h(n)={self.h()} g(n)={self.g()}\n" + \
               str(self.board[:3]) + "\n" + \
               str(self.board[3:6]) + "\n" + \
               str(self.board[6:]) + "\n"

# 초기 상태
puzzle = [8, 3, 5, 1, 6, 4, 7, 0, 5]

# 목표 상태
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

# open 리스트는 우선순위 큐로 생성한다.
open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, goal, 0))
closed_list = []
count = 0

while not open_queue.empty():
    current = open_queue.get()
    count += 1
    print(count)
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    for state in current.expand(current.depth + 1):
        if state not in closed_list:
            open_queue.put(state)
    closed_list.append(current)
else:
    print("탐색 실패")
