import pyxel #type: ignore
import function
import char
import laser

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 128

EASY = "easy"
NORMAL = "normal"
HARD = "hard"
HELL = "hell"

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="mouse_game")
        pyxel.load("asset.pyxres")
        pyxel.mouse(True)
        self.START_SCENE= "START"
        self.PLAY_SCENE = "PLAY"
        self.MENU_SCENE = "MENU"
        self.game_level = EASY
        self.EASY = EASY
        self.NORMAL = NORMAL
        self.HARD = HARD
        self.HELL = HELL
        self.current_scene = self.MENU_SCENE
        self.char_x = SCREEN_WIDTH // 2 - 8
        self.char_y = SCREEN_HEIGHT * 4 // 5
        self.laser_random = -1
        self.laser_number = 0
        self.character = char.Character(self.char_x, self.char_y)
        self.center_laser = laser.CenterLaser()
        self.left_laser = laser.LeftLaser()
        self.right_laser = laser.RightLaser()

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.current_scene == self.MENU_SCENE:
            function.update_menu_scene(self)
        elif self.current_scene == self.START_SCENE:
            function.update_start_scene(self)
        else:
            function.update_play_scene(self)

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()


    def draw(self):
        if self.current_scene == self.MENU_SCENE:
            function.draw_menu_scene(self)
        elif self.current_scene == self.START_SCENE:
            function.draw_start_scene(self)
        elif self.current_scene == self.PLAY_SCENE:
            function.draw_play_scene(self)

App()