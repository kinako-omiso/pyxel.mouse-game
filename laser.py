import pyxel #type: ignore

class Struct_Laser:
    save_x = [] #これなくてもいい、asseteファイル上のレーザーのx座標は一個前のx座標+width+1で求められるから。今回はバグ抑制のために使う。
    save_y = [0, 0, 0, 0, 0, 0]
    save_hight = []
    save_width = []
    draw_x = []
    draw_y = [58, 49, 38, 23, 3, 0]
    is_collision_active = False

class CenterLaser:
    def __init__(self):
        #中央レーザーの構造体を作成
        self.center_laser = Struct_Laser()
        self.center_laser.save_x = [0, 5, 12, 21, 34, 55]
        self.center_laser.save_hight = [11, 29, 51, 80, 121, 128]
        self.center_laser.save_width = [4, 6, 8, 12, 20, 66]
        self.center_laser.draw_x = [62, 61, 60, 58, 54, 30]
        self.laser_number = 0

        self.laytimer = -1


    def update(self):
       pass

    def draw(self, laser_number,i):
        if laser_number ==0 and i <6:
            x = self.center_laser.draw_x[i]
            y = self.center_laser.draw_y[i]
            u = self.center_laser.save_x[i]
            v = self.center_laser.save_y[i]
            w = self.center_laser.save_width[i] 
            h = self.center_laser.save_hight[i]
            pyxel.blt(x, y, 2, u, v, w, h, pyxel.COLOR_BLACK)
            if i == 5:
                laser_number = 1
                return laser_number
        else:
            pass


class LeftLaser:
    def __init__(self):
            #レーザーの構造体を作成
            self.left_laser = Struct_Laser()
            self.left_laser.save_x = [0, 5, 12, 21, 34,55]
            self.left_laser.save_y = [128, 128, 128, 128, 128, 128]
            self.left_laser.save_hight = [11, 29, 51, 80, 121, 128]
            self.left_laser.save_width = [4, 6, 8, 12, 20, 29]
            self.left_laser.draw_x = [66, 71, 78, 86, 96, 99]

            self.laytimer = -1


    def update(self):
        if self.is_collision==True:
            self.laytimer = -1

    def draw(self, laser_number,i):
        if laser_number ==0 and i<6:
            x = self.left_laser.draw_x[i]
            y = self.left_laser.draw_y[i]
            u = self.left_laser.save_x[i]
            v = self.left_laser.save_y[i]
            w = self.left_laser.save_width[i] 
            h = self.left_laser.save_hight[i]
            pyxel.blt(x, y, 2, u, v, w, h, pyxel.COLOR_BLACK)
            if i == 5:
                laser_number = 1
        else:
            pass


class RightLaser:
    def __init__(self):
        #中央レーザーの構造体を作成
        self.right_laser = Struct_Laser()
        self.right_laser.save_x = [0, 5, 12, 21, 34,183]
        self.right_laser.save_hight = [11, 29, 51, 80, 121, 128]
        self.right_laser.save_width = [4, 6, 8, 12, 20, 29]
        self.right_laser.draw_x = [58, 51, 43, 30, 13, 0]
       

        self.laytimer = -1


    def update(self):
        if self.is_collision==True:
            self.laytimer = -1

    def draw(self,laser_number,i):
        if laser_number ==0 and i <6:
            x=self.right_laser.draw_x[i]
            y=self.right_laser.draw_y[i] 
            u=self.right_laser.save_x[i]
            v=self.right_laser.save_y[i]
            w=self.right_laser.save_width[i] 
            h=self.right_laser.save_hight[i]
            pyxel.blt(x, y, 2, u, v, w, h, pyxel.COLOR_BLACK)
            if i == 5:
                laser_number = 1
        else:
            pass



       