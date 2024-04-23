# This is a sample Python script.
from util import *
import time
import pyautogui
import argparse
parser = argparse.ArgumentParser(prog="FFXIV-LeveResolver",description="automate accepting and submiting carrot leve quests")
parser.add_argument('-c','--count')

def find_category():
    button = pyautogui.locateOnScreen("assets/category.png", confidence=0.9)
    return button

def find_carrot():
    button = pyautogui.locateOnScreen("assets/carrot.png", confidence=0.8)
    return button

def reenter_select_menu():
    # Exit and reenter select menu inorder to deal with randomized image match failure

    key_interval()
    pyautogui.press("esc")
    #Exiting select menu
    key_interval()
    down()
    key_interval()
    #Move focus to second item
    enter()
    key_interval()
    #Reenter select menu

def select_carrot():
    button = find_carrot()
    while button == None :
        reenter_select_menu()
        key_interval()
        select_category()
        button = find_carrot()

    pyautogui.click(button)
    print("Click Carrot\n")
    key_interval()
    enter()
    key_interval()
    print("Focus\n")
    enter()
    key_interval()
    print("Focus on Confirm\n")
    enter()
    key_interval()
    print("confirm\n")
    enter()
    key_interval()
    print("Exit selection menu\n")
    exit()
    key_interval()
    print("Exit conversation menu\n")
    exit()
    key_interval()


def select_category():
    button = find_category()
    while button == None:
        reenter_select_menu()
        button = find_category()
    pyautogui.click(button)
    key_interval()
    pyautogui.click(button)
    pyautogui.click(button)

def turn_right():
    key_interval()
    pyautogui.keyDown('right')
    time.sleep(0.6)
    pyautogui.keyUp('right')

def turn_left():
    key_interval()
    pyautogui.keyDown('left')
    time.sleep(0.6)
    pyautogui.keyUp('left')

def submit():
    for _ in range(10):
        key_interval()
        enter()
    key_interval()

def ask():
    #Select and Skip Conversation
    for _ in range(3):
        time.sleep(time_short_sleep()*2)
        enter()

    key_interval()
    down()
    key_interval()
    enter()

def do_one_loop():
    time.sleep(2)
    select_category()
    select_carrot()
    turn_right()
    submit()
    turn_left()
    ask()

if __name__ == '__main__':
    #select_category()
    args = parser.parse_args()
    time.sleep(5)
    for _ in range(args.count):
        do_one_loop()
