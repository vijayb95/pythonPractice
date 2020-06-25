def sudoku2(grid):
    n = len(grid)
    parallelGrid = list(zip(*grid))
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                if grid[i].count(grid[i][j]) > 1: return False
                elif parallelGrid[i].count(grid[i][j]) > 1: return False
    return threeCheck(grid)
            
def threeCheck(grid):
    grid1 = []
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            for i in range(k, k+3):
                for j in range(l, l+3):
                    grid1.append(grid[i][j])
            if gridCheck(grid1): grid1.clear()
            else: return False  
    return True

def gridCheck(grid):
    for i in range(8):
        for j in range(i+1, 9):
            if grid[i] == grid[j] and grid[i] != ".": return False
    return True

if __name__ == "__main__":
    grid = [[".",".",".","1","4",".",".","2","."], 
            [".",".","6",".",".",".",".",".","."], 
            [".",".",".",".",".",".",".",".","."], 
            [".",".","1",".",".",".",".",".","."], 
            [".","6","7",".",".",".",".",".","9"], 
            [".",".",".",".",".",".","8","1","."], 
            [".","3",".",".",".",".",".",".","6"], 
            [".",".",".",".",".","7",".",".","."], 
            [".",".",".","5",".",".",".","7","."]]
    sudoku2(grid)