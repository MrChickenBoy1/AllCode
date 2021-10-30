import pyautogui
import time
import keyboard

speed = 1
clicks = 5
run = False
speed = float(input ("What speed do you want? (in seconds)"))
print ("")
print ("Speed noted")

clicks = int(input("How many clicks do you want? (00 for infinity"))

if clicks != 00:

    for i in range (clicks):
        pyautogui.click()
        time.sleep(speed)

if clicks == 00:
    run = True
    while run == True:
        pyautogui.click()
        time.sleep(speed)