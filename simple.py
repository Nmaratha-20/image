import pyautogui as p
import time

#this code is to open an image from forder called pictures


p.moveTo(99,748)
p.click(99,748)
p.typewrite("file explorer",.25)
time.sleep(1)
p.typewrite(['enter'])
time.sleep(2)

p.moveTo(956,169)

p.click(956,159)
p.click(button='right',clicks=1)
p.click(986,164)
p.click(1104,181)
p.click(button='right',clicks=2,interval=0.1)


