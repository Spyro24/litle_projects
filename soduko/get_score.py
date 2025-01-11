import time
import classes

def score(input_sudoku_string):
    grid = []
    #create the grid
    for y in range(9):
        grid.append([])
        for x in range(9):
            grid[y].append(classes.Cell())
            
    #insert default soduko
    counter = 0
    for y in range(9):
        for x in range(9):
            number = int(input_sudoku_string[counter])
            counter += 1
            if number > 0:
                grid[y][x].set_num(number)
    
    solve = classes.Solver(grid)
    rc = 0
    limit = 100
    start_time = time.time()
    while 1:
        rc += 1
        solved = True
        error = False
        solve.xy()
        solve.box()
        solve.single_number_box()
        solve.single_number_row()
        for y in range(9):
            for x in range(9):
                if grid[y][x].get_num_count() > 1:
                    solved = False
                    break
                if grid[y][x].get_num_count() == 0:
                    error = True
            if not solved:
                break
        if error:
            return ("", 0)
            break
        if solved:
            return ("", round((time.time() - start_time) * (rc * 2) * 1000))
            break
        if rc > limit:
            break
        
if __name__ == "__main__":
    print(score("000000000000003085001020000000507000004000100090000000500000073002010000000040009"))
    print(score("004708000007010800000040012000000070015000046609000080020004003000560000000003520"))
    print(score("060200000090400120000050006000760400020009005000001607081070000200000304000500000"))
    print(score("900057600040080010010400070070000405468000000000600000020300001003008000007020308"))
