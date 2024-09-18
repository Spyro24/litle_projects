import pygame as p

class Mazeviewer():
    def __init__(self, maze_width, maze_height):
        self.main_res = 7
        self.height = maze_height
        self.width = maze_width
        self.res_without_pivot = self.main_res - 1
        self.vertex = int(self.res_without_pivot / 2)
        self.window = p.display.set_mode((maze_width * self.main_res, maze_height * self.main_res))
        self.colors = [(255,255,255), (0,0,0)]
        self.window.fill(self.colors[0])
        
    def draw_rect(self, pos, faces):
        x = self.main_res * pos[0]
        y = self.main_res * pos[1]
        x += self.vertex
        y += self.vertex
        self.window.set_at((x,y), self.colors[0])
        if int(faces[0]) == 1:
            p.draw.line(self.window, self.colors[1], (x - self.vertex, y - self.vertex), (x + self.vertex, y - self.vertex))
        if int(faces[1]) == 1:
            p.draw.line(self.window, self.colors[1], (x + self.vertex, y - self.vertex), (x + self.vertex, y + self.vertex))
        if int(faces[2]) == 1:
            p.draw.line(self.window, self.colors[1], (x - self.vertex, y + self.vertex), (x + self.vertex, y + self.vertex))
        if int(faces[3]) == 1:
            p.draw.line(self.window, self.colors[1], (x - self.vertex, y - self.vertex), (x - self.vertex, y + self.vertex))
            
    def load_maze(self, file):
        self.maze = []
        maze_file = open(file, "br")
        for x in range(self.height):
            self.maze.append([])
            for y in range(0, int(self.width), 2):
                cur_byte = maze_file.read(1)
                cur_string = bin(int.from_bytes(cur_byte, "big"))
                cur_string = str(cur_string)
                #print(cur_string)
                cur_string = cur_string.split("b")
                st = cur_string[1]
                empty_string = ""
                for n in range(8 - len(st)):
                    empty_string += "0"
                s = empty_string + st
                self.draw_rect((x,y + 1),(s[0],s[1],s[2],s[3]))
                self.draw_rect((x,y),(s[4],s[5],s[6],s[7]))
            
    def export_to_png(self, file):
        p.image.save(self.window, file)
        
if __name__ == "__main__":
    app = Mazeviewer(int(input("X: ")), int(input("Y: ")))
    app.load_maze(input("Maze file input: "))
    #app.draw_rect((0,0),(1,0,0,0))
    p.display.flip()
    app.export_to_png(input("Maze png filename ") + ".png")
    p.quit()
