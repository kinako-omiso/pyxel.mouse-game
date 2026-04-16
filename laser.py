import pyxel

class Laser:
    def __init__(self):
        self.laytimer = -1

    def update(self):
        if self.is_collision==True:
            self.laytimer = -1

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        # 4フレーム(0, 1, 2, 3)をループ (10フレームごとに次の絵へ)
        frame_index = (pyxel.frame_count // 10) % 6  
        # 画像(バンク0)の中での、横と縦の位置を計算
        col = frame_index % 2  # 横の位置 (0 か 1)
        row = frame_index // 2 # 縦の位置 (0 か 1) 
        # 128ピクセルずつズラすための座標計算
        u = col * 128
        v = row * 128
        # バンク0の(u, v)から 128x128 ピクセルを切り出して、画面の(0, 0)に描画
        pyxel.blt(0, 0, 2, u, v, 128, 128)