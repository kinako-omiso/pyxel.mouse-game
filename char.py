import pyxel #type: ignore

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
        self.x = max(0, min(self.x, 112))
    
    def draw(self):
        cycle_frame = pyxel.frame_count % 120
        if cycle_frame < 60:
            is_blink = False
        else:
            blink_step = (cycle_frame - 60) // 15
            if blink_step % 2 == 0:
                is_blink = True
            else:
                is_blink = False
        # 判定を使って実際に描画を分ける
        if is_blink:
            # 点滅用（差分）の画像を描画
            # (座標 x, y や画像の切り出し位置などは適当に合わせる)
            pyxel.blt(self.x, self.y, 2, 168, 160, 16, 16, pyxel.COLOR_GRAY)
        else:
            # 通常時の画像を描画
            pyxel.blt(self.x, self.y, 2, 128, 160, 16, 16, pyxel.COLOR_GRAY)