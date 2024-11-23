import webbrowser
import pyautogui as pa
import time
pa.PAUSE = 1

def trivia(url=0):
    url = 'https://opentdb.com'
    webbrowser.open(url)
trivia()

time.sleep(3)
pa.click(x=1218, y=147) # Browser
pa.click(x=822, y=239) # Digitar
pa.write('Science: Computers')
pa.click(x=1001, y=236) #selecionar categoria
pa.write('Category')
pa.press('enter')
pa.click(x=1141, y=236) #Search
pa.scroll(-99999)