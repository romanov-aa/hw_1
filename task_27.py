#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
   a = 1
   move_right()
   while not wall_is_on_the_right():
       fill_cell()
       for j in range(a):
           if wall_is_on_the_right():
               return
           else:
              move_right()
       a=a+1



   pass


if __name__ == '__main__':
    run_tasks()
