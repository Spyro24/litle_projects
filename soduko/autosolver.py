import classes
import time

file = open("hard_sudokus.txt", "r")

solve_time = time.time()
solved_ = 0
_error = 0
to_hard = 0
avg_steps = 0
max_steps = 0

while True:
    for n in range(100):
        default_sodoku = file.readline()
        grid = []
        counter = 0

        #create the grid
        for y in range(9):
            grid.append([])
            for x in range(9):
                 grid[y].append(classes.Cell())
        
        #insert default soduko
        for y in range(9):
            for x in range(9):
                number = int(default_sodoku[counter])
                counter += 1
                if number > 0:
                    grid[y][x].set_num(number)
        

    
        solve = classes.Solver(grid)
        rc = 0
        limit = 25
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
                _error += 1
                break
            if solved:
                solved_ += 1
                avg_steps += rc
                if max_steps < rc:
                    max_steps = rc
                break
            if rc > limit:
                to_hard += 1
                break
    print("Solved:", str(solved_))
    print("Hard:", str(to_hard))
    print("Error:", str(_error))
    print("Time:", str(time.time() - solve_time))
    print("AVG Steps:", str(avg_steps / solved_))
    print("MAX Steps:", str(max_steps))
    print()