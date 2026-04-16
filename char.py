import pyxel

class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dest_x = x
        self.is_destination = True

    def move(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            self.dest_x = pyxel.mouse_x
            self.is_destination = False
        if self.is_destination == False:
            if self.dest_x-5 > self.x:
                self.x += 2
            elif self.dest_x+5 < self.x:
                self.x -=2
            else:
                self.is_destination = True
        
    def update(self):
        self.move()
    
    def draw(self):
        pyxel.blt(self.x, self.y, 2, 0, 0, 16, 16, pyxel.COLOR_BLACK)