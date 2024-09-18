#import pygame as p
import time
import random

def convert_to_int(bin_string):
    inp = bin_string 
    output = 0
    if len(bin_string) < 8:
        while len(inp) < 8:
            inp += "0"
    for n in range(0, 8):
        if inp[n] == "1":
            output += 2**(n)
    return output
    
class Maze():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = []
        self.max_punishment = 10
        if  not (width % 2 == 0):
            raise BaseException("Width of the maze must be a multiple of 2")
        
    def gen_empty_maze(self):
        for y in range(self.height):
            self.maze.append([])
            for x in range(self.width):
                self.maze[y].append([])
                for n in range(4):
                    self.maze[y][x].append(1)
                self.maze[y][x].append(False)
                
    def gen_maze_hak(self):
        #The Hunt and Kill algorithm for maze generating
        print("Maze generator chosed: Hunt and Kill")
        x_pos = random.randint(0, self.width - 1)
        y_pos = random.randint(0, self.height - 1)
        print("Start pos: (" + str(x_pos) + ", " + str(y_pos) + ")")
        direction = None
        last_dir = None
        stuck = False
        run = True
        h_x = 0
        h_y = 0
        last_x = None
        last_y = None
        punishment = 0
        while run:
            if not stuck: #move the mazer
                last_y = y_pos
                last_x = x_pos
                direction = random.randint(0,3)
                if direction == 0: #UP
                    if last_dir != direction:
                        if y_pos > 0:
                            if self.maze[y_pos - 1][x_pos][4] == False:
                                last_dir = 2
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(direction)
                                self.maze[y_pos][x_pos].insert(direction,0)
                                y_pos -= 1
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(last_dir)
                                self.maze[y_pos][x_pos].insert(last_dir,0)
                elif direction == 2: #Down
                    if last_dir != direction:
                        if y_pos < self.height - 1:
                            if self.maze[y_pos + 1][x_pos][4] == False:
                                last_dir = 0
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(direction)
                                self.maze[y_pos][x_pos].insert(direction,0)
                                y_pos += 1
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(last_dir)
                                self.maze[y_pos][x_pos].insert(last_dir,0)
                elif direction == 1: #Right
                    if last_dir != direction:
                        if x_pos < self.width - 1:
                            if self.maze[y_pos][x_pos + 1][4] == False:
                                last_dir = 3
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(direction)
                                self.maze[y_pos][x_pos].insert(direction,0)
                                x_pos += 1
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(last_dir)
                                self.maze[y_pos][x_pos].insert(last_dir,0)
                if direction == 3: #Left
                    if last_dir != direction:
                        if x_pos > 0:
                            if self.maze[y_pos][x_pos - 1][4] == False:
                                last_dir = 1
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(direction)
                                self.maze[y_pos][x_pos].insert(direction,0)
                                x_pos -= 1
                                self.maze[y_pos][x_pos].pop(4)
                                self.maze[y_pos][x_pos].append(True)
                                self.maze[y_pos][x_pos].pop(last_dir)
                                self.maze[y_pos][x_pos].insert(last_dir,0)
                                
                up = y_pos - 1
                down = y_pos + 1
                left = x_pos - 1
                right = x_pos  + 1
                if up < 0:
                    up = 0
                if left < 0:
                    left = 0
                if down >= self.height:
                    down = self.height - 1
                if right >= self.width:
                    right = self.width - 1
                
                #check if the mazer get stuck
                if self.maze[up][x_pos][4] and self.maze[down][x_pos][4] and self.maze[y_pos][left][4] and self.maze[y_pos][right][4]:
                    stuck = True
                    #print("stuck")
                
                '''
                if ((last_x == x_pos) and (last_y == y_pos)):
                    #print("Punish")
                    punishment += 1
                    if punishment > self.max_punishment:
                        stuck = True
                        punishment = 0
        '''
            if stuck:
                h_x = 0
                h_y = 0
                search = True
                while search:
                    if self.maze[h_y][h_x][4]:
                        up = h_y - 1
                        down = h_y + 1
                        left = h_x - 1
                        right = h_x + 1
                        if up < 0:
                            up = 0
                        if left < 0:
                            left = 0
                        if down >= self.height:
                            down = self.height - 1
                        if right >= self.width:
                            right = self.width - 1
                        if not self.maze[up][h_x][4] or not self.maze[down][h_x][4] or  not self.maze[h_y][left][4] or not self.maze[h_y][right][4]:
                            print(h_x, h_y)
                            x_pos = h_x
                            y_pos = h_y
                            search = False
                            stuck = False
                            last_dir = None 
                    
                    h_x += 1
                    if h_x >= self.width:
                        h_x = 0
                        h_y +=1
                    if h_y >= self.height:
                        search = False
                        run = False
                        print("Finish")
                    
                        
                    
    def export(self, file):
        save = open(file, "bw")
        for save_x in range(len(self.maze)):
            for save_y in range(0, int(len(self.maze[save_x])), 2):
                save_string = ""
                for n in range(2):
                    for _ in range(4):
                        save_string += str(self.maze[save_x][save_y + n][_])
                save.write(int.to_bytes(convert_to_int(save_string), 1, "big"))

if __name__ == "__main__":
    try:
        print("Setting up maze")
        maze = Maze(int(input("X: ")), int(input("Y: ")))
        print("gen empty maze")
        t = time.time()
        maze.gen_empty_maze()
        print("Genrating took " + str(time.time() - t) + " seconds")
        maze.gen_maze_hak()
    finally:
        maze.export(input("Maze filename"))
    
