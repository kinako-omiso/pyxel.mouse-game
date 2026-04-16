import pyxel
import char

def reset_game(self):
    self.char_x = 0
    self.char_y = 0

def update_menu_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        self.current_scene = self.START_SCENE

def update_start_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        self.current_scene = self.PLAY_SCENE

def update_play_scene(self):
    if pyxel.btnp(pyxel.KEY_R):
        reset_game(self)
    self.character.update()
    

def draw_menu_scene(self):
    pyxel.cls(pyxel.COLOR_DARK_BLUE)
    pyxel.text(pyxel.width//10, pyxel.height//10, "CLICK TO START", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 40, "EASY", pyxel.COLOR_YELLOW)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 60, "NORMAL", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 80, "HARD", pyxel.COLOR_RED)


def draw_start_scene(self): 
    pyxel.blt(0, 0, 0, 0, 0, pyxel.width, pyxel.height)
    pyxel.text(50, 50, "START", 7)

def draw_play_scene(self):
    pyxel.cls(pyxel.COLOR_BLACK)
    # 4フレーム(0, 1, 2, 3)をループ (10フレームごとに次の絵へ)
    frame_index = (pyxel.frame_count // 5) % 8   
    # 画像(バンク0)の中での、横と縦の位置を計算
    bank = frame_index // 4  # バンクの位置 (0 か 1)
    local_frame = frame_index % 4
    col = local_frame % 2  # 横の位置 (0 か 1)
    row = local_frame // 2 # 縦の位置 (0 か 1) 
    # 128ピクセルずつズラすための座標計算
    u = col * 128
    v = row * 128
    # バンク0の(u, v)から 128x128 ピクセルを切り出して、画面の(0, 0)に描画
    pyxel.blt(0, 0, bank, u, v, 128, 128)
    self.character.draw()
    

