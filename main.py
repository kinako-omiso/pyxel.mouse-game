import pyxel 
import function

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

EASY = "easy"
NORMAL = "normal"
HARD = "hard"
HELL = "hell"

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="mouse_game")
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