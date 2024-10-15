import sys
from enum import Enum
from time import sleep, time
from datetime import datetime
import random
import threading

import pyautogui
from pynput.keyboard import Listener

# Variables -> Change nothing here!!!
class PRESS_EVENT(Enum):
    # Letters
    A = lambda: pyautogui.press('a')
    B = lambda: pyautogui.press('b')
    C = lambda: pyautogui.press('c')
    D = lambda: pyautogui.press('d')
    E = lambda: pyautogui.press('e')
    F = lambda: pyautogui.press('f')
    G = lambda: pyautogui.press('g')
    H = lambda: pyautogui.press('h')
    I = lambda: pyautogui.press('i')
    J = lambda: pyautogui.press('j')
    K = lambda: pyautogui.press('k')
    L = lambda: pyautogui.press('l')
    M = lambda: pyautogui.press('m')
    N = lambda: pyautogui.press('n')
    O = lambda: pyautogui.press('o')
    P = lambda: pyautogui.press('p')
    # Q = lambda: pyautogui.press('q') # Q is needed for quitting
    R = lambda: pyautogui.press('r')
    S = lambda: pyautogui.press('s')
    T = lambda: pyautogui.press('t')
    U = lambda: pyautogui.press('u')
    V = lambda: pyautogui.press('v')
    W = lambda: pyautogui.press('w')
    X = lambda: pyautogui.press('x')
    Y = lambda: pyautogui.press('y')
    Z = lambda: pyautogui.press('z')
    
    # Numbers
    NUM_0 = lambda: pyautogui.press('0')
    NUM_1 = lambda: pyautogui.press('1')
    NUM_2 = lambda: pyautogui.press('2')
    NUM_3 = lambda: pyautogui.press('3')
    NUM_4 = lambda: pyautogui.press('4')
    NUM_5 = lambda: pyautogui.press('5')
    NUM_6 = lambda: pyautogui.press('6')
    NUM_7 = lambda: pyautogui.press('7')
    NUM_8 = lambda: pyautogui.press('8')
    NUM_9 = lambda: pyautogui.press('9')
    
    # Function keys
    F1 = lambda: pyautogui.press('f1')
    F2 = lambda: pyautogui.press('f2')
    F3 = lambda: pyautogui.press('f3')
    F4 = lambda: pyautogui.press('f4')
    F5 = lambda: pyautogui.press('f5')
    F6 = lambda: pyautogui.press('f6')
    F7 = lambda: pyautogui.press('f7')
    F8 = lambda: pyautogui.press('f8')
    F9 = lambda: pyautogui.press('f9')
    F10 = lambda: pyautogui.press('f10')
    F11 = lambda: pyautogui.press('f11')
    F12 = lambda: pyautogui.press('f12')
    
    # Special keys
    SPACE = lambda: pyautogui.press('space')
    ENTER = lambda: pyautogui.press('enter')
    TAB = lambda: pyautogui.press('tab')
    ESC = lambda: pyautogui.press('esc')
    BACKSPACE = lambda: pyautogui.press('backspace')
    DELETE = lambda: pyautogui.press('delete')
    SHIFT = lambda: pyautogui.press('shift')
    CTRL = lambda: pyautogui.press('ctrl')
    ALT = lambda: pyautogui.press('alt')
    
    # Arrow keys
    LEFT_ARROW = lambda: pyautogui.press('left')
    RIGHT_ARROW = lambda: pyautogui.press('right')
    UP_ARROW = lambda: pyautogui.press('up')
    DOWN_ARROW = lambda: pyautogui.press('down')
    
    # Mouse actions
    LEFT_CLICK = lambda: pyautogui.click(button='left')
    RIGHT_CLICK = lambda: pyautogui.click(button='right')
    MIDDLE_CLICK = lambda: pyautogui.click(button='middle')
    DOUBLE_CLICK = lambda: pyautogui.doubleClick()
    SCROLL_UP = lambda: pyautogui.scroll(10)  # Scroll up
    SCROLL_DOWN = lambda: pyautogui.scroll(-10)  # Scroll down
    
    def execute(self):
        self.value()


##########################################################
# CHANGABLE THESE VARIABLES IF YOU WANT RUN THIS main.py #
##########################################################

press_event = PRESS_EVENT.LEFT_CLICK    # - press_event: PRESS_EVENT Enum or None Value for defining key to press
rel_pos_x = 0.75    # - rel_pos_x: Float x position of the event in percentage (0.0 - 1.0)
rel_pos_y = 0.05    # - rel_pos_y: Float y position of the event in percentage (0.0 - 1.0)
time_fire_minutes = 0.6 # 60.0    # - time_fire_minutes: Float minutes before the next event press fires
timeout = None    # - timeout: None or Float value in minutes for quitting the program after the given minutes
use_random_walk = True    # - random_walk_activated: Boolean if the mouse should be random moving between the press events
time_buffer = 5.0    # - time_buffer: Float seconds to wait between every loop

##########################################################


# listens keyboard
def start_listener():
    with Listener(on_release=on_release) as listener:
        listener.join()

def on_release(key):
    try:
        if key.char == "q":
            sys.exit(-1)
            print(f"\n\nQuitting because you ended the program! ({get_current_time_as_string()})\nI hope you was successfull :)")
    except AttributeError:
        pass

def get_current_time_as_string():
    now = datetime.now()
    return f"{now.hour:02}:{now.minute:02} {now.day:02}.{now.month:02}.{now.year:04}"

def random_float(min, max):
    return (random.random()*(max-min))+min

def mouse_activity(press_event:PRESS_EVENT, rel_pos_x=0.0, rel_pos_y=0.0, time_fire_minutes=60, timeout=None, random_walk_activated=True, time_buffer=1.0):
    """
    Presses a key or mouse button every X minutes. Can move the mouse during the time between.

    - press_event: PRESS_EVENT Enum or None Value for defining key to press
    - rel_pos_x: Float x position of the event in percentage (0.0 - 1.0)
    - rel_pos_y: Float y position of the event in percentage (0.0 - 1.0)
    - time_fire_minutes: Float minutes before the next event press fires
    - timeout: None or Float value in minutes for quitting the program after the given minutes
    - random_walk_activated: Boolean if the mouse should be random moving between the press events
    - time_buffer: Float seconds to wait between every loop
    """

    print(f"Welcome to the Mouse-Activity Program! ({get_current_time_as_string()})")
    print("init activity...")
    
    # get screen-size and define goal position
    screen_width, screen_height = pyautogui.size()

    goal_x = rel_pos_x * (screen_width-1)
    goal_y = rel_pos_y * (screen_height-1)

    # start keyboard listener for quitting the program
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()

    # set init values
    pyautogui.FAILSAFE = False
    SHOULD_RUN = True
    fire = False
    last_fire = start_time = time()
    cur_random_walk_direction = [random_float(min=-1, max=1), random_float(min=-1, max=1)]

    # start program loop
    print(f"starts running the activity every {time_fire_minutes} minutes. ({get_current_time_as_string()})")
    while SHOULD_RUN:
        # check if timeout
        if timeout is not None and (time()-start_time)/60 >= timeout:
            print(f"Quitting because timeout reached! ({get_current_time_as_string()})")
            sys.exit(-1)

        # check if should fire now
        cur_time_diff = (time() - last_fire) / 60
        if cur_time_diff >= time_fire_minutes:
            fire = True
            last_fire = time()

        if fire:
            # move to goal position
            print("CHECKPOINT 1")
            pyautogui.moveTo(goal_x, goal_y, duration=1) 
            cur_x, cur_y = pyautogui.position()
            print("CHECKPOINT 2")
            while cur_x != goal_x and cur_y != goal_y:
                sleep(0.5)

            print("CHECKPOINT 3")

            # press button
            if press_event is not None:
                press_event.execute()

            fire = False
            print(f"Fired! ({get_current_time_as_string()})")

            cur_random_walk_direction = [random_float(min=-1, max=1), random_float(min=-1, max=1)]

        # random walk
        if random_walk_activated:
            x, y = pyautogui.position()
            if (x <= 0 or x >= screen_width-1) or (y <= 0 or y >= screen_height-1):
                cur_random_walk_direction = [random_float(min=-1, max=1), random_float(min=-1, max=1)]
            else:
                pyautogui.moveRel(screen_width*0.05*cur_random_walk_direction[0], screen_height*0.005*cur_random_walk_direction[0], duration=1) 

        sleep(time_buffer)


if __name__ == "__main__":
    mouse_activity(
        press_event=press_event,
        rel_pos_x=rel_pos_x,
        rel_pos_y=rel_pos_y,
        time_fire_minutes=time_fire_minutes,
        timeout=timeout,
        random_walk_activated=use_random_walk,
        time_buffer=time_buffer
    )


