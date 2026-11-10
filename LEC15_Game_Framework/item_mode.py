import os

import game_framework
import game_world
from pico2d import *


image = None


def init():
    global image
    image = load_image(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'item_select.png')
    )


def finish():
    global image
    image = None


def handle_events():
    get_events()


def update():
    pass  # 월드를 업데이트하지 않음 → 게임 정지


def render():
    clear_canvas()
    game_world.render()  # 멈춘 게임 화면을 그대로 그림
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()


def pause():
    pass


def resume():
    pass
