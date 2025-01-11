class Cell():
    def __init__(self):
        self.numbers = [1,2,3,4,5,6,7,8,9]
        
    def get_num_count(self):
        return len(self.numbers)
    
    def get_num(self):
        return self.numbers[0]
    
    def set_num(self, num):
        self.numbers = [num]
    
    def remove_num(self, num):
        try:
            self.numbers.pop(self.numbers.index(num))
        except:
            pass
        
    def get_numbers(self):
        return self.numbers
    
    def contains(self, num):
        try:
            self.numbers.index(num)
        except:
            return False
        return True
        
class Solver():
    def __init__(self, init_soduko):
        self.grid = init_soduko
        self.boxes = []
        c = 0
        for y in range(0,9,3):
            for x in range(0,9,3):
                self.boxes.append([])
                for yy in range(3):
                    for xx in range(3):
                        self.boxes[c].append(self.grid[y+yy][x+xx])
                c += 1
            
        
    def xy(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x].get_num_count() == 1:
                    cell_num = self.grid[y][x].get_num()
                    for w in range(9):
                        if w != x:
                            self.grid[y][w].remove_num(cell_num)
                    for h in range(9):
                        if h != y:
                            self.grid[h][x].remove_num(cell_num)
                            
    def box(self):
        for box in self.boxes:
            mc = len(box)
            for n in range(mc):
                if box[n].get_num_count() == 1:
                    ins = box[n].get_num()
                    for i in range(mc):
                        if i != n:
                            box[i].remove_num(ins)
    
    def single_number_box(self):
        for box in self.boxes:
            mc = len(box)
            for n in range(mc):
                if box[n].get_num_count() > 1:
                    numb = box[n].get_numbers()
                    for num in numb:
                        sn = True
                        for v in range(9):
                            if n != v:
                                if box[v].contains(num):
                                    sn = False
                        if sn:
                            box[n].set_num(num)
                            break
                            
    def single_number_row(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x].get_num_count() > 1:
                    numb = self.grid[y][x].get_numbers()
                    cell_num = self.grid[y][x].get_num()
                    for num in numb:
                        row = True
                        collum = True
                        for w in range(9):
                            if w != x:
                                if self.grid[y][w].contains(num):
                                    row = False
                                    break
                        for h in range(9):
                            if h != y:
                                if self.grid[h][x].contains(num):
                                    collum = False
                                    break
                        if row or collum:
                            self.grid[y][x].set_num(num)
                            break
                            
    def xwing(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x].get_num_count() > 1:
                    numb = self.grid[y][x].get_numbers()
                    for num in numb:
                        x_marked_rows = [x]
                        y_marked_rows = [y]
                        for n in range(9):
                            if n != x:
                                if self.grid[y][n].contains(num):
                                    x_marked_rows.append(n)
                                    
                        for n in range(9):
                            if n != y:
                                if self.grid[n][x].contains(num):
                                    y_marked_rows.append(n)
                                    
                        print(x_marked_rows, y_marked_rows, (x, y), num)
