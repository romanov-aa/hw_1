#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right()
    move_down()
    for i in range(4):
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_right(2)
        fill_cell()
        move_up()
        move_right(3)
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()
    move_up()
    move_left(2)
    pass


if __name__ == '__main__':
    run_tasks()
