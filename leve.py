# This is a sample Python script.
import time
import pyautogui
import argparse
parser = argparse.ArgumentParser(prog="FFXIV-LeveResolver",description="automate accepting and submiting carrot leve quests")
parser.add_argument('-c','--count')

def get_sleep_time():
    return 0.4

def sleep_random_time():
    time.sleep((get_sleep_time()))

def find_category():
    button = pyautogui.locateOnScreen("assets/category.png", confidence=0.9)
    return button

def find_carrot():
    button = pyautogui.locateOnScreen("assets/carrot.png", confidence=0.8)
    return button

def reenter_select_menu():
    # Exit and reenter select menu inorder to deal with randomized image match failure

    sleep_random_time()
    pyautogui.press("esc")
    #Exiting select menu
    sleep_random_time()
    pyautogui.press('num2')
    #Move focus to second item
    sleep_random_time()
    pyautogui.press('num0')
    #Reenter select menu

def select_carrot():
    button = find_carrot()
    while button == None :
        reenter_select_menu()
        sleep_random_time()
        select_category()
        button = find_carrot()

    pyautogui.click(button)
    print("Click Carrot\n")
    sleep_random_time()
    pyautogui.press('num0')
    sleep_random_time()
    print("Focus\n")
    pyautogui.press('num0')
    sleep_random_time()
    print("Focus on Confirm\n")
    pyautogui.press('num0')
    sleep_random_time()
    print("confirm\n")
    pyautogui.press('num0')
    sleep_random_time()
    print("Exit selection menu\n")
    pyautogui.press("esc")
    sleep_random_time()
    print("Exit conversation menu\n")
    pyautogui.press("esc")


def select_category():
    button = find_category()
    while button == None:
        reenter_select_menu()
        button = find_category()
    pyautogui.click(button)
    sleep_random_time()
    pyautogui.click(button)
    pyautogui.click(button)

def turn_right():
    sleep_random_time()
    pyautogui.keyDown('right')
    time.sleep(0.6)
    pyautogui.keyUp('right')

def turn_left():
    sleep_random_time()
    pyautogui.keyDown('left')
    time.sleep(0.6)
    pyautogui.keyUp('left')

def submit():
    for _ in range(10):
        sleep_random_time()
        pyautogui.press('num0')
    sleep_random_time()

def ask():
    #Select and Skip Conversation
    for _ in range(3):
        time.sleep(get_sleep_time()*2)
        pyautogui.press('num0')

    sleep_random_time()
    pyautogui.press('num2')
    sleep_random_time()
    pyautogui.press('num0')

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
