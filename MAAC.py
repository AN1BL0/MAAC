import pyautogui
import time
#import rich.progress
from rich.progress import track

print("         MAAC\n       ver. 0.5\n    Made By AN1BL0\n\n")
time.sleep(3)

b = int(input("1 - Режим кликера" + "\n2 - Minecraft exp farm\n" + "3 - Собственные настройки\n"))

if b == 1:
    n = int(input("Сколько программа будет работать? (сек)\n"))
    print("Старт через 5 сек\n")
    time.sleep(5)
    for step in track(range(n), description="Кликаем..."):
        time.sleep(0)
        pyautogui.leftClick()

     
if b == 2:
    n = int(input("Сколько программа будет работать? (сек)\n"))
    print("Старт через 5 сек\n")
    time.sleep(5)
    for step in track(range(n), description="Кликаем..."):
        time.sleep(0.5)
        pyautogui.leftClick()

if b == 3:
    c = float(input("Введите желаемую задержку между кликами (сек)\n"))
    n = int(input("Сколько программа будет работать? (сек)\n"))
    print("Старт через 5 сек\n")
    time.sleep(5)
    for step in track(range(n), description="Кликаем..."):
        time.sleep(c)
        pyautogui.leftClick()