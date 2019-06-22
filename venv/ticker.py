from datetime import datetime as dt
import time
import tkinter as tk

# while True:
#     print(dt.today().strftime("%H:%m:%S"))
#     sleep(1)


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RobotoClock")
        self.label = tk.Label(text="clock")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now, font=("Roboto", 44))
        self.root.after(1000, self.update_clock)

app=App()
