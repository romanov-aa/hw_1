#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if not wall_is_on_the_right():
        move_right()
    else:
        if not wall_is_above():
            move_up()
        else:
            if not wall_is_on_the_left():
                move_left()
            else:
                if not wall_is_beneath():
                    move_down()
    
            
        
    pass


if __name__ == '__main__':
    run_tasks()
