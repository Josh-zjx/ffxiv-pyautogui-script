# This is a sample Python script.
from util import *
import time

def select_nth_employee(n):
    for _ in range(n):
        down()
        key_interval()
    enter()
    wait_conversation()
    enter()
    wait_conversation()

def collect_and_reset_explore():
    # select explore and enter
    for _ in range(5):
        down()
        key_interval()
    enter()
    key_interval()

    # select reset explore
    left()
    key_interval()
    enter()
    key_interval()

    # confirm explore
    left()
    key_interval()
    enter()
    wait_conversation()
    enter()
    wait_conversation()

def exit_employee():
    exit()
    key_interval()
    exit()
    wait_conversation()

def collect_nth_employee(n):
    select_nth_employee(n)
    collect_and_reset_explore()
    exit_employee()

def do_test():
    enter()

def do_one_loop():
    enter()
    for i in range(9):
        collect_nth_employee(i)
        wait_conversation()

if __name__ == '__main__':
    time.sleep(5)
    do_one_loop()
