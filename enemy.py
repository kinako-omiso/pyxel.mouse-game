import pyxel
import random

class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = -1  # -1 は「出現していない」状態
        self.last_state = -1
        self.spawn_start_frame = 0 # スポーンを開始した時間を記録
        self.terepo=False

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
            self.state = elapsed // 60 # 60フレームごとに進む

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
                    if self.x< 16 or self.x > 128 or self.y < 16 or self.y > 120:
                        # 画面外に出ないように調整
                        self.x = max(16, min(self.x, 128))
                        self.y = max(16, min(self.y, 120))
                elif self.state > 2:
                    # 状態2が終わったら消える（または次の行動へ）
                    self.state = -1 
                
                self.last_state = self.state


class StraightBullet3D:
    def __init__(self, target_px, target_py):
        self.X = 0       # 左右中央
        self.Y = -20     # 少し上（ボスの顔や手の高さ）
        self.Z = 100     # 遠く奥

        # --- 2. 3D空間上のターゲット地点 (自機の今の2D位置を3Dの座標系に変換) ---
        # プレイエリアの中心(64, 64)を原点(0,0)にするための変換
        self.target_X = target_px - 64
        self.target_Y = target_py - 64
        self.target_Z = 1  # 手前（プレイヤーがいる場所）

        # --- 3. 速度の計算 (何フレームで自機に届かせるか) ---
        duration = 45.0  # 数字が小さいほど速い弾になる
        self.vx = (self.target_X - self.X) / duration
        self.vy = (self.target_Y - self.Y) / duration
        self.vz = (self.target_Z - self.Z) / duration
        
        self.active = True

    def update(self):
        # 3D空間を等速直線運動
        self.X += self.vx
        self.Y += self.vy
        self.Z += self.vz
        
        # プレイヤーを通り過ぎるか、地面に着いたら消滅
        if self.Z <= self.target_Z:
            self.active = False

    def draw(self):
        # --- 4. 3D座標を2Dスクリーン座標に変換 (投影) ---
        # 焦点距離(f)を64とすると、Z=1のとき3D座標がそのまま2D座標のズレになる
        f = 64
        sx = (self.X * f) / self.Z + 64
        sy = (self.Y * f) / self.Z + 64
        
        # 手前に来るほど大きくする
        size = 10 / self.Z
        
        color = pyxel.COLOR_WHITE if self.Z < 50 else pyxel.COLOR_GRAY
        pyxel.circ(sx, sy, size, color)

class CircleEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.bullets_active = False
        self.bullets_collision = False
        self.bullet = None  # 追加：最初は弾がない状態にしておく

    def update(self, char_x, char_y):
        super().update()
        
        # 状態2になったとき、弾がまだ出ていないなら新しい弾を発射
        if self.state == 2 and not self.bullets_active:
            self.bullet = StraightBullet3D(char_x, char_y)
            self.bullets_active = True
            
        # 弾がアクティブな間は、毎フレーム弾の座標を更新する
        if self.bullets_active and self.bullet:
            self.bullet.update()
            # 弾が寿命（地面到達）を迎えたらフラグを戻す
            if not self.bullet.active:
                self.bullets_active = False

        # 注意: これは「敵本体」との当たり判定になっている。
        # 弾との当たり判定にするなら self.bullet のスクリーン座標と比較する必要がある。
        if not self.bullets_collision and char_x > self.x - 8 and char_x < self.x + 8 and char_y > self.y - 8 and char_y < self.y + 8:
            self.bullets_active = False
            self.bullets_collision = True

    def draw(self):
        # 敵本体の描画
        if self.state == 0:
            if pyxel.frame_count % 30 == 0:
                pyxel.blt(self.x-2, self.y-2, 2, 170, 144, 4, 4, pyxel.COLOR_BLACK)
            else:
                pyxel.blt(self.x-2, self.y-2, 2, 170, 128, 4, 4, pyxel.COLOR_GRAY)
                
        elif self.state == 1:
            if pyxel.frame_count % 30 == 0:
                pyxel.blt(self.x-4, self.y-4, 2, 160, 144, 8, 8, pyxel.COLOR_BLACK)
            else:
                pyxel.blt(self.x-4, self.y-4, 2, 160, 128, 8, 8, pyxel.COLOR_GRAY)
                
        elif self.state == 2:
            if pyxel.frame_count % 30 == 0:
                pyxel.blt(self.x-8, self.y-8, 2, 144, 144, 16, 16, pyxel.COLOR_BLACK)
            else:   
                pyxel.blt(self.x-8, self.y-8, 2, 144, 128, 16, 16, pyxel.COLOR_GRAY)
                
        # 弾の描画（弾が存在してアクティブな時だけ描画する）
        if self.bullets_active and self.bullet:
            self.bullet.draw()


class SquareEnemy(Enemy):
    def __init__(self):
        super().__init__()

    def update(self):
        super().update()

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
        
        if self.state == 0:
            
                pyxel.blt(self.x-2, self.y-2, 2, 199, 144, 4, 4, pyxel.COLOR_BLACK)
            else:
                pyxel.blt(self.x-2, self.y-2, 2, 199, 128, 4, 4, pyxel.COLOR_GRAY)
                
        elif self.state == 1:
            if pyxel.frame_count % 30 == 0:
                pyxel.blt(self.x-4, self.y-4, 2, 189, 144, 8, 8, pyxel.COLOR_BLACK)
            else:
                pyxel.blt(self.x-4, self.y-4, 2, 189, 128, 8, 8, pyxel.COLOR_GRAY)
                
        elif self.state == 2:
            if pyxel.frame_count % 30 == 0:
                pyxel.blt(self.x-8, self.y-8, 2, 173, 144, 16, 16, pyxel.COLOR_BLACK)
            else:   
                pyxel.blt(self.x-8, self.y-8, 2, 173, 128, 16, 16, pyxel.COLOR_GRAY)
            