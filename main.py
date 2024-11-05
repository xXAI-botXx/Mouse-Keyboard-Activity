import sys
from enum import Enum
from time import sleep, time
from datetime import datetime
import random
import threading

import pyautogui
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button

# Variables -> Change nothing here!!! Scroll a bit down :)
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
    Q = lambda: pyautogui.press('q') 
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
    # ESC = lambda: pyautogui.press('esc') # Escape key is needed for quitting
    BACKSPACE = lambda: pyautogui.press('backspace')
    DELETE = lambda: pyautogui.press('delete')
    SHIFT = lambda: pyautogui.press('shift')
    STRG = lambda: pyautogui.press('ctrl')
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

def press_event_to_key(event_: PRESS_EVENT):
    """
    Maps a PRESS_EVENT to a corresponding keyboard Key or KeyCode.
    """
    # Mapping PRESS_EVENT items to keyboard keys
    key_mapping = {
        PRESS_EVENT.A: KeyCode.from_char('a'),
        PRESS_EVENT.B: KeyCode.from_char('b'),
        PRESS_EVENT.C: KeyCode.from_char('c'),
        PRESS_EVENT.D: KeyCode.from_char('d'),
        PRESS_EVENT.E: KeyCode.from_char('e'),
        PRESS_EVENT.F: KeyCode.from_char('f'),
        PRESS_EVENT.G: KeyCode.from_char('g'),
        PRESS_EVENT.H: KeyCode.from_char('h'),
        PRESS_EVENT.I: KeyCode.from_char('i'),
        PRESS_EVENT.J: KeyCode.from_char('j'),
        PRESS_EVENT.K: KeyCode.from_char('k'),
        PRESS_EVENT.L: KeyCode.from_char('l'),
        PRESS_EVENT.M: KeyCode.from_char('m'),
        PRESS_EVENT.N: KeyCode.from_char('n'),
        PRESS_EVENT.O: KeyCode.from_char('o'),
        PRESS_EVENT.P: KeyCode.from_char('p'),
        PRESS_EVENT.Q: KeyCode.from_char('q'),
        PRESS_EVENT.R: KeyCode.from_char('r'),
        PRESS_EVENT.S: KeyCode.from_char('s'),
        PRESS_EVENT.T: KeyCode.from_char('t'),
        PRESS_EVENT.U: KeyCode.from_char('u'),
        PRESS_EVENT.V: KeyCode.from_char('v'),
        PRESS_EVENT.W: KeyCode.from_char('w'),
        PRESS_EVENT.X: KeyCode.from_char('x'),
        PRESS_EVENT.Y: KeyCode.from_char('y'),
        PRESS_EVENT.Z: KeyCode.from_char('z'),
        
        # Numbers
        PRESS_EVENT.NUM_0: KeyCode.from_char('0'),
        PRESS_EVENT.NUM_1: KeyCode.from_char('1'),
        PRESS_EVENT.NUM_2: KeyCode.from_char('2'),
        PRESS_EVENT.NUM_3: KeyCode.from_char('3'),
        PRESS_EVENT.NUM_4: KeyCode.from_char('4'),
        PRESS_EVENT.NUM_5: KeyCode.from_char('5'),
        PRESS_EVENT.NUM_6: KeyCode.from_char('6'),
        PRESS_EVENT.NUM_7: KeyCode.from_char('7'),
        PRESS_EVENT.NUM_8: KeyCode.from_char('8'),
        PRESS_EVENT.NUM_9: KeyCode.from_char('9'),
        
        # Function keys
        PRESS_EVENT.F1: Key.f1,
        PRESS_EVENT.F2: Key.f2,
        PRESS_EVENT.F3: Key.f3,
        PRESS_EVENT.F4: Key.f4,
        PRESS_EVENT.F5: Key.f5,
        PRESS_EVENT.F6: Key.f6,
        PRESS_EVENT.F7: Key.f7,
        PRESS_EVENT.F8: Key.f8,
        PRESS_EVENT.F9: Key.f9,
        PRESS_EVENT.F10: Key.f10,
        PRESS_EVENT.F11: Key.f11,
        PRESS_EVENT.F12: Key.f12,
        
        # Special keys
        PRESS_EVENT.SPACE: Key.space,
        PRESS_EVENT.ENTER: Key.enter,
        PRESS_EVENT.TAB: Key.tab,
        PRESS_EVENT.BACKSPACE: Key.backspace,
        PRESS_EVENT.DELETE: Key.delete,
        PRESS_EVENT.SHIFT: Key.shift,
        PRESS_EVENT.STRG: Key.ctrl,
        PRESS_EVENT.ALT: Key.alt,
        
        # Arrow keys
        PRESS_EVENT.LEFT_ARROW: Key.left,
        PRESS_EVENT.RIGHT_ARROW: Key.right,
        PRESS_EVENT.UP_ARROW: Key.up,
        PRESS_EVENT.DOWN_ARROW: Key.down,

        # Mouse button mappings
        PRESS_EVENT.LEFT_CLICK: Button.left,
        PRESS_EVENT.RIGHT_CLICK: Button.right,
        PRESS_EVENT.MIDDLE_CLICK: Button.middle,
    }
    
    return key_mapping.get(event_, None)


SHOULD_RUN = True


##########################################################
# CHANGABLE THESE VARIABLES IF YOU WANT RUN THIS main.py #
##########################################################

press_event = PRESS_EVENT.LEFT_CLICK    # PRESS_EVENT Enum or None Value for defining key to press
cancel_event = PRESS_EVENT.STRG         # PRESS_EVENT Use only keyboard events for this, it will define the cancel condition
pick_position = True    # Boolean decides whether to pick a position or use the given position
rel_pos_x = 0.75    # Float x position of the event in percentage (0.0 - 1.0)
rel_pos_y = 0.05    # Float y position of the event in percentage (0.0 - 1.0)
start_time_buffer = 5.0    # Float in seconds after starting/picking a position first starts the program after the given seconds
time_fire_minutes = 60.0    # Float minutes before the next event press fires
timeout = None    # None or Float value in minutes for quitting the program after the given minutes
use_random_walk = True    # Boolean if the mouse should be random moving between the press events
time_buffer = 5.0    # Float seconds to wait between every loop

##########################################################


def keyboard_listener_func(key):
    global SHOULD_RUN
    global cancel_event
    try:
        if key == Key.ctrl_l or key == Key.ctrl_r:
            key = Key.ctrl
        # print(f"Result:{press_event_to_key(cancel_event)}")
        # print(f"You pressed:{key}\n")
        if key == keyboard.Key.esc or key == press_event_to_key(cancel_event):
            SHOULD_RUN = False
            print(f"\n\nQuitting because you ended the program! ({get_current_time_as_string()})\nI hope you was successfull :)")
    except AttributeError:
        pass

def mouse_listener_func(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
        if button == mouse.Button.left or button == mouse.Button.right:
            return False  # stops the listener

def get_current_time_as_string():
    now = datetime.now()
    return f"{now.hour:02}:{now.minute:02} {now.day:02}.{now.month:02}.{now.year:04}"

def random_float(min, max):
    return (random.random()*(max-min))+min

def update_random_walk():
    cur_random_walk_direction = [random_float(min=-1, max=1), random_float(min=-1, max=1)]
    cur_random_walk_direction[0] = cur_random_walk_direction[0] + 1 if cur_random_walk_direction[0] >= 0 else cur_random_walk_direction[0] - 1
    cur_random_walk_direction[1] = cur_random_walk_direction[1] + 1 if cur_random_walk_direction[1] >= 0 else cur_random_walk_direction[1] - 1
    return cur_random_walk_direction  

def get_random_pos():
    screen_width, screen_height = pyautogui.size()
    screen_width -= 1
    screen_height -= 1
    return [random.randint(0, screen_width), random.randint(0, screen_height)]

def mouse_activity(press_event:PRESS_EVENT, 
                   pick_position=True, 
                   rel_pos_x=0.0, 
                   rel_pos_y=0.0, 
                   start_time_buffer=3.0, 
                   time_fire_minutes=60, 
                   timeout=None, 
                   random_walk_activated=True, 
                   time_buffer=1.0):
    """
    When starting the picker
    Presses a key or mouse b
    When starting the pickerutton every X minutes. Can move the mouse during the time between.

    When starting the picker, you have to move your mouse to the goal position and press left mouse or right mouse button.

    - press_event: PRESS_EVENT Enum or None Value for defining key to press
    - pick_position: Boolean decides whether to pick a position or use the given position
    - rel_pos_x: Float x position of the event in percentage (0.0 - 1.0)
    - rel_pos_y: Float y position of the event in percentage (0.0 - 1.0)
    - start_time_buffer: Float in seconds after starting/picking a position first starts the program after the given seconds
    - time_fire_minutes: Float minutes before the next event press fires
    - timeout: None or Float value in minutes for quitting the program after the given minutes
    - random_walk_activated: Boolean if the mouse should be random moving between the press events
    - time_buffer: Float seconds to wait between every loop
    """
    global SHOULD_RUN

    print(f"Welcome to the Mouse-Activity Program! ({get_current_time_as_string()})")
    print("init activity...")
    
    # get screen-size and define goal position
    screen_width, screen_height = pyautogui.size()

    if pick_position:
        print("Picking now the position...\n    -> Move your mouse to the goal position and press left mouse or right mouse button.")

        # waiting for picking
        with mouse.Listener(on_click=mouse_listener_func) as listener:
            listener.join()

        goal_x, goal_y = pyautogui.position()
    else:
        goal_x = rel_pos_x * (screen_width-1)
        goal_y = rel_pos_y * (screen_height-1)
    print(f"Goal Position: {goal_x}/{goal_y}")

    escape_listener = keyboard.Listener(on_release=keyboard_listener_func)
    escape_listener.start()

    # set init values
    pyautogui.FAILSAFE = False
    SHOULD_RUN = True
    fire = False
    last_fire = start_time = time()
    # cur_random_walk_direction = update_random_walk()
    cur_random_goal = get_random_pos()

    # wait for beginning
    print(f"Program starts in round about {start_time_buffer} seconds.")
    while time() - start_time < start_time_buffer:
        sleep(0.1)

    # start program loop
    print(f"starts running the activity every {time_fire_minutes} minutes. ({get_current_time_as_string()})")
    while SHOULD_RUN:

        # check if timeout
        if timeout is not None and (time()-start_time)/60 >= timeout:
            print(f"Quitting because timeout reached! ({get_current_time_as_string()})")
            sys.exit(0)

        # check if should fire now
        cur_time_diff = (time() - last_fire) / 60
        if cur_time_diff >= time_fire_minutes:
            fire = True
            last_fire = time()

        if fire:
            # move to goal position
            pyautogui.moveTo(goal_x, goal_y, duration=1) 
            cur_x, cur_y = pyautogui.position()

            while cur_x != goal_x and cur_y != goal_y:
                sleep(0.5)
                pyautogui.moveTo(goal_x, goal_y, duration=1) 
                cur_x, cur_y = pyautogui.position()

            # press button
            if press_event is not None:
                press_event()

            fire = False
            print(f"Fired! ({get_current_time_as_string()})")

            # cur_random_walk_direction = update_random_walk()
            cur_random_goal = get_random_pos()

        # random walk
        if random_walk_activated:
            x, y = pyautogui.position()

            if x==cur_random_goal[0] and y==cur_random_goal[1]:
                cur_random_goal = cur_random_goal = get_random_pos()

            pyautogui.moveTo(cur_random_goal[0], cur_random_goal[1], duration=2) 
        
            # if (x <= 0 or x >= screen_width-1) or (y <= 0 or y >= screen_height-1):
            #     cur_random_walk_direction = update_random_walk()
                
            # pyautogui.moveRel(screen_width*0.1*cur_random_walk_direction[0], screen_height*0.1*cur_random_walk_direction[1], duration=1) 

        sleep(time_buffer)


if __name__ == "__main__":
    mouse_activity(
        press_event=press_event,
        rel_pos_x=rel_pos_x,
        rel_pos_y=rel_pos_y,
        time_fire_minutes=time_fire_minutes,
        timeout=timeout,
        random_walk_activated=use_random_walk,
        time_buffer=time_buffer,
        start_time_buffer=start_time_buffer
    )


