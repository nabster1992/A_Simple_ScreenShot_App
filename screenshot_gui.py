from unicodedata import name
import pyautogui
import time
import tkinter as tk

def screenshot():
    time.sleep(1)
    name = time.time()
    name = r'C:\Users\Nabizzle\Desktop\python_projects\screenshot_app_project/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

root = tk.Tk() # initializes variable name root
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text='Take Screenshot', command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="Quit", command= exit)
close.pack(side=tk.LEFT)

root.mainloop()