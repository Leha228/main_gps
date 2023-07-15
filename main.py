from config import *
from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title(TITLE)
        self.root.geometry(GEOMETRY)
        self.root.minsize(MIN_WIDTH, MIN_HEIGHT)
        self.root.configure(background=BACKGROUND)
        self.add_btn('FirstButton', command=self.replace_theme)
        self.root.mainloop()

    def add_btn(self, name, command) -> None:
        btn = ttk.Button(text=name, command=command)
        btn.pack()
        btn.configure(style="")

    def replace_theme(self):
        global is_lite
        is_lite = not is_lite
        self.check_theme()
        self.root.configure(background=BACKGROUND)

    def check_theme(self):
        global BACKGROUND
        BACKGROUND = THEME_LITE['background'] if is_lite else THEME_BLACK['background']


if __name__ == "__main__":
    App()
