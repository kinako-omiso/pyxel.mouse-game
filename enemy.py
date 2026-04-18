import pyxel
import random

class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = 0 # frame_countの代わりに状態として管理
        self.last_state = -1 # 前回の状態を保存用

    def update(self):
        # 5フレームごとに 0, 1, 2 を繰り返す
        self.state = (pyxel.frame_count // 5) % 3

        # 状態が変わった瞬間だけ座標を更新する
        if self.state != self.last_state:
            if self.state == 0:
                self.x = random.randint(56, 56+16)
                self.y = random.randint(56, 56+16)
            elif self.state == 1:
                self.x = random.randint(24, 95)
                self.y = random.randint(24, 95)
            elif self.state == 2:
                self.x = random.randint(0, 128)
                self.y = random.randint(0, 128)
            
            self.last_state = self.state # 更新完了を記録

    def draw(self):
        # bltのサイズ引数（w, h）が 1, 4, 8 とかなり小さいけど、ドット絵のサイズに合わせて調整してね
        if self.state == 0:
            pyxel.blt(self.x, self.y, 2, 144, 128, 1, 1, pyxel.COLOR_BLACK)
        elif self.state == 1:
            pyxel.blt(self.x, self.y, 2, 144, 128, 4, 4, pyxel.COLOR_BLACK)
        elif self.state == 2:
            pyxel.blt(self.x, self.y, 2, 144, 128, 8, 8, pyxel.COLOR_BLACK)