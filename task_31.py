#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_8_30():
    for i in range(5):
        while not wall_is_on_the_left():
            move_left()
            while not wall_is_beneath():
                 move_down()
        while not wall_is_on_the_right():
           move_right()
           while not wall_is_beneath():
              move_down()
    while not wall_is_on_the_left():
        move_left()

    pass


if __name__ == '__main__':
    run_tasks()
