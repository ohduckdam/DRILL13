import os

import game_framework
import game_world
from pico2d import *


image = None


def init():
    global image
    image = load_image(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pause.png')
    )


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()  # play_mode로 복귀
            return


def update():
    pass  # 월드를 업데이트하지 않음 → 일시정지


def render():
    clear_canvas()
    game_world.render()  # 멈춘 게임 화면을 그대로 그림
    image.draw(400, 300)  # 그 위에 일시정지 이미지
    update_canvas()


def pause():
    pass


def resume():
    pass
