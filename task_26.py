#!/usr/bin/python3

from pyrob.api import *


def plus():
    fill_cell()
    move_down()
    fill_cell()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up(2)


@task(delay=0.001)
def task_2_4():
    i = 3

    for i in range(2):
        move_right()
        for i in range(10):
            plus()
            move_right(1)
            if not wall_is_on_the_right():
                move_right(3)
            else:
                move_down(4)
                move_left(1)
                for i in range(10):
                    plus()
                    move_left(1)
                    if not wall_is_on_the_left():
                        move_left(3)
                    else:
                        move_down(4)
    move_right()
    for i in range(10):
        plus()
        move_right(1)
        if not wall_is_on_the_right():
            move_right(3)
    while not wall_is_on_the_left():
        move_left()










if __name__ == '__main__':
    run_tasks()
