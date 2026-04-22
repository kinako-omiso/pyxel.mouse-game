import pyxel #type: ignore
import random
#hp実装

def reset_game(self):
    self.char_x = pyxel.width // 2 - 8
    self.char_y = pyxel.height * 4 // 5
    self.laser_random = -1
    self.laser_number = 0
    self.is_collision = False
    self.hp = 3
    self.already_hit = False
    self.current_scene = self.MENU_SCENE

def update_menu_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        self.current_scene = self.START_SCENE

def update_start_scene(self):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        self.current_scene = self.PLAY_SCENE

def update_play_scene(self):
    if self.is_collision == True:
            if self.hp == 0:
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.reset_game()
                    self.current_scene = self.MENU_SCENE
                    self.remove(self.circle_enemy)
                    return
                
            else:
                self.hp -= 1
                self.is_collision = False
    else:
        center_x = self.character.x + 8
        self.frame_count = (pyxel.frame_count // 5) % 7

        if pyxel.frame_count % 35 == 0:  # 30フレームごとにレーザー発射
            self.laser_random = random.randint(0, 2)
            self.laser_number = 0 
            self.already_hit = False

        if self.frame_count == 6:
            self.laser_number = 1

        if self.laser_number == 0 and (self.frame_count == 4 or self.frame_count == 5):
            if self.already_hit==False:
                if self.laser_random == 0 and 54 <  center_x  < 70:
                    self.is_collision = True
                    self.already_hit = True
                elif self.laser_random == 1 and 96 <  center_x  < 116:
                    self.is_collision = True
                    self.already_hit = True
                elif self.laser_random == 2 and 13 <  center_x  < 33:
                    self.is_collision = True
                    self.already_hit = True
        self.circle_enemy.update(self.char_x,self.char_y)
        self.character.update()
        self.squreEnemy.update()
    

      

       
    

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
        pyxel.cls(pyxel.COLOR_ORANGE)
        pyxel.rect(132, 4, 35, 120, pyxel.COLOR_BLACK)
        pyxel.rect(0, 0, 128, 128, pyxel.COLOR_BLACK)
        pyxel.text(pyxel.width//4+10, pyxel.height//10 + 40, "GAME OVER", pyxel.COLOR_WHITE)
        
        if self.hp > 0:
            #背景描画
            # 8フレーム(0, 1, 2, 3)をループ (5フレームごとに次の絵へ)
            frame_index = (pyxel.frame_count // 5) % 8   
            # 画像(バンク0)の中での、横と縦の位置を計算
            bank = frame_index // 4  # バンクの位置 (0 か 1)
            local_frame = frame_index % 4
            col = local_frame % 2
            row = local_frame // 2
            # 128ピクセルずつズラすための座標計算
            u = col * 128
            v = row * 128
            # バンク0の(u, v)から 128x128 ピクセルを切り出して、画面の(0, 0)に描画
            pyxel.blt(0, 0, bank, u, v, 128, 128)
            self.character.draw()
            
            # レーザー描画
            if self.laser_random == 0:
                self.center_laser.draw(self.laser_number, self.frame_count)
            elif self.laser_random == 1:
                self.left_laser.draw(self.laser_number, self.frame_count)
            elif self.laser_random == 2:
                self.right_laser.draw(self.laser_number, self.frame_count)

        for i in range(self.hp):
            # x座標を 132 から始めて、10ピクセルずつズラして描画
            # (1個目:132, 2個目:142, 3個目:152)
            pyxel.blt(135 + i * 10, 4, 2, 128, 128, 9, 9)
        for i in range(3 - self.hp):
            pyxel.blt(135 + (self.hp + i) * 10, 4, 2, 135, 136, 9, 9)

        self.circle_enemy.draw()
        self.squreEnemy.draw()