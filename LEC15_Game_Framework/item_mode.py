import os

import game_framework
import game_world
import play_mode
from ball import BALL_BIG, BALL_NONE, BALL_SMALL
from pico2d import *


image = None

KEY_TO_BALL_MODE = {
    SDLK_0: BALL_NONE,   # 공 없음
    SDLK_1: BALL_SMALL,  # 작은 공
    SDLK_2: BALL_BIG,    # 큰 공
    SDLK_KP_0: BALL_NONE,  # 숫자 키패드도 지원
    SDLK_KP_1: BALL_SMALL,
    SDLK_KP_2: BALL_BIG,
}


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
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key in KEY_TO_BALL_MODE:
            play_mode.boy.set_ball_mode(KEY_TO_BALL_MODE[event.key])
            game_framework.pop_mode()  # 선택 후 play_mode로 복귀
            return
        if event.type == SDL_KEYDOWN and event.key in (SDLK_ESCAPE, SDLK_i):
            game_framework.pop_mode()  # 선택 없이 play_mode로 복귀
            return


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
