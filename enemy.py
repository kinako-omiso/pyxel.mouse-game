import pyxel
import random

class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = -1  # -1 は「出現していない」状態
        self.last_state = -1
        self.spawn_start_frame = 0 # スポーンを開始した時間を記録

    def update(self):
        # 90フレームごとにスポーンを開始する
        if pyxel.frame_count % 90 == 0:
            if self.state == -1: # すでに出現中なら無視（重なり防止）
                self.state = 0
                self.spawn_start_frame = pyxel.frame_count

        # スポーン中（stateが0以上）の処理
        if self.state >= 0:
            # スポーン開始からの経過時間で状態（0, 1, 2）を決める
            elapsed = pyxel.frame_count - self.spawn_start_frame
            self.state = elapsed // 15 # 15フレームごとに進む

            # 状態が変わった瞬間だけ座標を更新する
            if self.state != self.last_state:
                if self.state == 0:
                    self.x = random.randint(56, 56+16)
                    self.y = random.randint(56, 56+16)
                elif self.state == 1:
                    self.x = random.randint(self.x-20, self.x+20)
                    self.y = random.randint(self.y-20, self.y+20)
                    if self.x< 8 or self.x > 128 or self.y < 8 or self.y > 120:
                        # 画面外に出ないように調整
                        self.x = max(8, min(self.x, 128))
                        self.y = max(8, min(self.y, 120))
                elif self.state == 2:
                    self.x = random.randint(self.x-50, self.x+50)
                    self.y = random.randint(self.y-50, self.y+50)
                    if self.x< 8 or self.x > 128 or self.y < 8 or self.y > 120:
                        # 画面外に出ないように調整
                        self.x = max(8, min(self.x, 128))
                        self.y = max(8, min(self.y, 120))
                elif self.state > 2:
                    # 状態2が終わったら消える（または次の行動へ）
                    self.state = -1 
                
                self.last_state = self.state

    def draw(self):
        # state が -1（未出現）のときは何も書かない
        if self.state == 0:
            pyxel.blt(self.x-2, self.y-2, 2, 144, 128, 4, 4, pyxel.COLOR_BLACK)
        elif self.state == 1:
            pyxel.blt(self.x-4, self.y-4, 2, 144, 128, 8, 8, pyxel.COLOR_BLACK)
        elif self.state == 2:
            pyxel.blt(self.x-8, self.y-8, 2, 144, 128, 16, 16, pyxel.COLOR_BLACK)