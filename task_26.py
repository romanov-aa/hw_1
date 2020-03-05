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
    # цикл между строк
    while True:
        # цикл в нутри строки
        while True:
            if flag2:
                move_right()
            else:
                move_left()
            i += 1
            if i % 2 == 0:
                if flag:
                    flag = False
                else:
                    flag = True
                    continue
                plus()
            if wall_is_on_the_right() or wall_is_on_the_left():
                break
        # после строки
        i = 1
        flag = True
        flag2 = not flag2
        for _ in range(4):
            if wall_is_beneath():
                break
            else:
                move_down()
        if wall_is_beneath() and wall_is_on_the_right():
            while not wall_is_on_the_left():
                move_left()
            move_up(2)
            break





if __name__ == '__main__':
    run_tasks()
