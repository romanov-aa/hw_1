#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    while not wall_is_on_the_right():
        if not wall_is_above() and not wall_is_beneath():
            
            move_right()
        else:
            fill_cell()
            move_right()
            
    if wall_is_above() or wall_is_beneath():
        fill_cell()
        
    pass


if __name__ == '__main__':
    run_tasks()
