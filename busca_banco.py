import webbrowser
import pyautogui as pa
import time
pa.PAUSE = 2

def trivia(url=0):
    url = 'https://opentdb.com'
    webbrowser.open(url)
trivia()

time.sleep(3)
pa.click(x=1218, y=147) # Browser
pa.click(x=822, y=239) # Digitar
pa.write('Science: Computers')
pa.click(x=1141, y=236) #Search