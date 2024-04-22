# This is a sample Python script.
import random
import time
import pyautogui
import argparse
parser = argparse.ArgumentParser(prog="FFXIV-LeveResolver",description="automate accepting and submiting carrot leve quests")
parser.add_argument('-c','--count')

def down():
    sleep_random_time()
    pyautogui.press('num2')
    sleep_random_time()

def up():
    sleep_random_time()
    pyautogui.press('num8')
    sleep_random_time()

def exit():
    sleep_random_time()
    pyautogui.press('esc')
    sleep_random_time()

def left():
    sleep_random_time()
    pyautogui.press('num4')
    sleep_random_time()

def right():
    sleep_random_time()
    pyautogui.press('num2')
    sleep_random_time()

def enter():
    sleep_random_time()
    pyautogui.press('num0')
    sleep_random_time()

def get_sleep_time():
    return random.randint(4, 8) / 10.0

def sleep_random_time():
    time.sleep((get_sleep_time()))

def select_nth_employee(n):
    for _ in range(n):
        down()
    enter()
    time.sleep(1)
    enter()
    time.sleep(1)

def collect_and_reset_explore():
    # select explore and enter
    for _ in range(5):
        down()
    enter()

    # select reset explore
    left()
    enter()

    # confirm explore
    left()
    enter()
    time.sleep(1)
    enter()
    time.sleep(1)

def exit_employee():
    exit()
    exit()
    time.sleep(3)

def collect_nth_employee(n):
    select_nth_employee(n)
    collect_and_reset_explore()
    exit_employee()

def do_test():
    enter()
    collect_nth_employee(3)
    collect_nth_employee(5)

def do_one_loop():
    enter()
    for i in range(9):
        collect_nth_employee(i)
        time.sleep(1)

if __name__ == '__main__':
    time.sleep(5)
    do_one_loop()
