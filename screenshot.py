import pyautogui
import time

def screenshot():
    time.sleep(5)
    name = time.time()
    name = r'C:\Users\Nabizzle\Desktop\python_projects\screenshot_app_project/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

screenshot()