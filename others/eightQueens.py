board_size = 8
solution_count = 0
queen_list = [0] * board_size

def eight_queens(row: int):
    if row == board_size:
        global solution_count
        solution_count += 1
        print(queen_list)
    else:
        for i in range(board_size):
            if is_valid_pos(row, i):
                queen_list[row] = i
                eight_queens(row + 1)

def is_valid_pos(row: int, col: int) -> bool:
    left_up, right_up = col - 1, col + 1
    for cur_row in reversed(range(row)):
        if queen_list[cur_row] == col: return False
        if queen_list[cur_row] == left_up: return False
        if queen_list[cur_row] == right_up: return False
        left_up -= 1
        right_up += 1
    return True

if __name__ == '__main__':
    eight_queens(0)
    print(solution_count)