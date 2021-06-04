import pyautogui
import time

print("         MAAC\n       ver. 0.1\n    Made By AN1BL0\n\n")
time.sleep(5)

b = int(input("1 - just click" + "\n2 - Minecraft exp farm\n" + "3 - enter your settings\n"))

if b == 1:
    n = int(input("Enter duration (sec)\n"))
    print("Start in 5 sec\n")
    time.sleep(5)
    for x in range(n):
        time.sleep(0)
        pyautogui.leftClick()
     
if b == 2:
    n = int(input("Enter duration (sec)\n"))
    print("Start in 5 sec\n")
    time.sleep(5)
    for x in range(n):
        time.sleep(0.5)
        pyautogui.leftClick()

if b == 3:
    c = float(input("Enter delay (sec)\n"))
    n = int(input("Enter duration (sec)\n"))
    print("Start in 5 sec\n")
    time.sleep(5)
    for x in range(n):
        time.sleep(c)
        pyautogui.leftClick()       
