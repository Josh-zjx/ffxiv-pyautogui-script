# This is a sample Python script.
from util import *
import time
import pyautogui
import argparse
parser = argparse.ArgumentParser(prog="FFXIV-LeveResolver",description="automate accepting and submiting carrot leve quests")
parser.add_argument('-c','--count')

def find_category():
    # target image should be captured on deployment machine to correctly match option texture in game
    button = pyautogui.locateOnScreen("assets/category.png", confidence=0.95)
    return button

def find_carrot():
    # target image should be captured on deployment machine to correctly match option texture in game
    button = pyautogui.locateOnScreen("assets/carrot.png", confidence=0.85)
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
    wait_window_interaction()
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
    wait_window_interaction()
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
    wait_window_interaction()
    pyautogui.click(button)
    pyautogui.click(button)

def turn_right():
    key_interval()
    pyautogui.keyDown('right')
    time.sleep(0.65)
    pyautogui.keyUp('right')

def turn_left():
    key_interval()
    pyautogui.keyDown('left')
    time.sleep(0.65)
    pyautogui.keyUp('left')

def submit():

    # 7 enters to submit the first good in inventory
    # 1. select npc 
    # 2. enter conver 
    # 3. enter inv 
    # 4. select first item 
    # 5.confirm first item 
    # 6.submit item 
    # 7. confirm submit
    for _ in range(7):
        key_interval()
        enter()


    # slow conversation anime after submit good
    wait_conversation()

    # 3 enters to end submission
    # 1. exit conv
    # 2. exit system notification
    # 3. exit quest result
    for _ in range(3):
        key_interval()
        enter()
    key_interval()

def ask():
    #Select and Skip Conversation
    key_interval()
    enter()
    key_interval()
    enter()
    wait_conversation()
    enter()

    wait_window_interaction()
    down()
    key_interval()
    enter()
    wait_window_interaction()

def do_one_loop():
    #time.sleep(2)
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
