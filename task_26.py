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


@task(delay=0.02)
def task_2_4():
    i = 1
    flag = True
    flag2 = True
    while True:
        move_right()
        while True:

            plus()
            i += 1
            i % 2 == 0








if __name__ == '__main__':
    run_tasks()
