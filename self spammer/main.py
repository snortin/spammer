import pyautogui as gui

text = input('text: ')

print('running')

while True:
    gui.write(text)
    gui.press('enter')