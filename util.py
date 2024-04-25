# This is a sample Python script.
import random
import time
import pyautogui

def down():
    pyautogui.press('num2')

def up():
    pyautogui.press('num8')

def exit():
    pyautogui.press('esc')

def left():
    pyautogui.press('num4')

def right():
    pyautogui.press('num2')

def enter():
    pyautogui.press('num0')

#def time_short_sleep():
#    return random.randint(1, 3) / 10.0
#
#def time_long_sleep():
#    return 2

def wait_conversation():
    time.sleep(2)

def wait_window_interaction():
    time.sleep(0.5)

def key_interval():
    time.sleep(0.1)

if __name__ == '__main__':
    print("util shouldn't be used")
