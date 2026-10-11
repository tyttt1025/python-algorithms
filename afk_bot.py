import pyautogui as pag
import random
import time 

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    delay = random.randint(2, 5)
    pag.moveTo(x, y, 0.5)
    time.sleep(delay)