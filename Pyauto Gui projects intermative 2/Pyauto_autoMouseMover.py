import pyautogui as autoMouse
import random
import time

while True:
    x =random.randint(50,1200)
    y =random.randint(50,600)

    autoMouse.moveTo(x,y,0.5)
    time.sleep(0)