from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
            return
        else:
            boy.handle_event(event)



def init():
    global boy

    game_world.clear()
    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy, 1)

def update_world():
    game_world.update()


def update():
    update_world()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def render():
    draw()


def finish():
    global boy
    game_world.clear()
    boy = None


def pause():
    pass


def resume():
    pass