import os

import game_framework
from pico2d import *


image = None


def init():
    global image
    image_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'title.png'
    )
    image = load_image(image_path)


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            import play_mode
            game_framework.push_mode(play_mode)
            return


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def pause():
    pass


def resume():
    pass
