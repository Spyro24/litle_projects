import classes
import utime

default_sodoku = "000000000000003085001020000000507000004000100090000000500000073002010000000040009"
#default_sodoku = "700530000083006000009018637090007123607003084000004506900082010830000090004700308"
#default_sodoku = "009000000050070600810300000005083000000200700034900008000400910001000043080001506"
#default_sodoku = "840007530320050087007060294400902851095186073081340060602790345004501628030620709" #7
#default_sodoku = "000030040681000000900820001000004009500000000004600027002003005000700930000459070" #140
#default_sodoku = "706480300000090001009060000210004000800000040000000002000020730007000200008075060" #234
#default_sodoku = "300010208000800006400002000800000000009130740002007000000095000001720005000000009" #242
#default_sodoku = "000000200050009040701005000039070000160090020400006100008000906006000315000010000" #386
#default_sodoku = "004708000007010800000040012000000070015000046609000080020004003000560000000003520"

start_time = utime.time()
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
        number = int(default_sodoku[counter])
        counter += 1
        if number > 0:
            grid[y][x].set_num(number)
        
#print the init Soduko
def print_sd():
    for y in range(9):
        out = ""
        for x in range(9):
            if grid[y][x].get_num_count() == 1:
                out += str(grid[y][x].get_num()) + " "
            else:
                out += "_ "
        print(out)
    print()

def print_usd():
    for y in range(9):
        out = ""
        for x in range(9):
                out += str(grid[y][x].get_numbers()) + " "
        print(out)
    print()
    
solve = classes.Solver(grid)
print_sd()
#print_usd()
rc = 0
limit = 100
while 1:
    rc += 1
    solved = True
    error = False
    solve.xy()
    solve.box()
    solve.single_number_box()
    solve.single_number_row()
    #solve.xwing()
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
        print("This Sudoku is not solvable")
        break
    if solved:
        print_sd()
        print("solve steps: " + str(rc))
        break
    if rc > limit:
        print_sd()
        print_usd()
        break
print (utime.time() - start_time)