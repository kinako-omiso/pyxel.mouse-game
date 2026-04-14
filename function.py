import pyxel

def update_menu_scene(app):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        app.current_scene = app.START_SCENE

def update_start_scene(app):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        app.current_scene = app.PLAY_SCENE

def update_play_scene(app):
    pass

def draw_menu_scene(app):
    pyxel.cls(pyxel.COLOR_DARK_BLUE)
    pyxel.text(pyxel.width//10, pyxel.height//10, "CLICK TO START", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 40, "EASY", pyxel.COLOR_YELLOW)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 60, "NORMAL", pyxel.COLOR_WHITE)
    pyxel.text(pyxel.width//3+10, pyxel.height//10 + 80, "HARD", pyxel.COLOR_RED)


def draw_start_scene(app):
    pyxel.cls(pyxel.COLOR_BLACK) 
    pyxel.text(50, 50, "START", 7)

def draw_play_scene(app):
    pyxel.cls(pyxel.COLOR_BLACK)
    pyxel.text(50, 50, "PLAY", 7)