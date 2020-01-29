#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for i in range(13):
        fill_cell()
        move_down()
    move_right()
    move_up()
    for i in range(12):
        fill_cell()
        move_up()
    move_right()
    move_down(2)
    for i in range(11):
        fill_cell()
        move_down()
    move_right()
    move_up()
    for i in range(10):
        fill_cell()
        move_up()
    move_right()
    move_down(2)
    for i in range(9):
        fill_cell()
        move_down()
    move_right()
    move_up()
    for i in range(8):
        fill_cell()
        move_up()
    move_right()
    move_down(2)
    for i in range(7):
        fill_cell()
        move_down()
    move_right()
    move_up()
    for i in range(6):
        fill_cell()
        move_up()
    move_right()
    move_down(2)
    for i in range(5):
        fill_cell()
        move_down()
    move_right()
    move_up()
    for i in range(4):
        fill_cell()
        move_up()
    move_right()
    move_down(2)
    for i in range(3):
        fill_cell()
        move_down()
    move_right()
    move_up()
    for i in range(2):
        fill_cell()
        move_up()
    move_right()
    move_down(2)
    for i in range(1):
        fill_cell()
        move_down()
    while not wall_is_on_the_left():
        move_left()
    move_right()
    pass


if __name__ == '__main__':
    run_tasks()
