#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_5_10():
    for i in range(20):
       while not wall_is_on_the_right():
           fill_cell()
           move_right()
       if not wall_is_beneath():
           fill_cell()
           move_down()
       else:
           while not wall_is_on_the_left():
               fill_cell()
               move_left()
       while not wall_is_on_the_left():
           fill_cell()
           move_left()
       if not wall_is_beneath():
           fill_cell()
           move_down()        
    pass


if __name__ == '__main__':
    run_tasks()
