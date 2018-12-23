
def print_sudoku(grid):
    for i in range(9):
        for j in range(9):
            print grid[i][j],
        print

def find_empty_location(grid, l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def used_in_row(grid, row, num):
    for col in range(9):
        if grid[row][col] == num:
            return True
    return False

def used_in_col(grid, col, num):
    for row in range(9):
        if grid[row][col] == num:
            return True
    return False

def used_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if grid[row+i][col+j] == num:
                return True
    return False

def is_safe_location(grid, row, col, num):
    return (not used_in_row(grid, row, num) and not used_in_col(grid, col, num) 
        and not used_in_box(grid, row-row%3, col-col%3, num))


def solve_sudoku(grid):
    l = [0, 0]
    if not find_empty_location(grid, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if is_safe_location(grid, row, col, num):
            grid[row][col] = num
            
            # print "row: {}, col: {}, num: {}".format(row, col, num)

            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0

    return False


if __name__ == '__main__':
    grid = [[3,0,6,5,0,8,4,0,0], 
            [5,2,0,0,0,0,0,0,0], 
            [0,8,7,0,0,0,0,3,1], 
            [0,0,3,0,1,0,0,8,0], 
            [9,0,0,8,6,3,0,0,5], 
            [0,5,0,0,9,0,6,0,0], 
            [1,3,0,0,0,0,2,5,0], 
            [0,0,0,0,0,0,0,7,4], 
            [0,0,5,2,0,6,3,0,0]]

    if solve_sudoku(grid):
        print_sudoku(grid)
    else:
        print "Not possible!"
