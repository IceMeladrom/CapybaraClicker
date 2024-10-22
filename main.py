import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Game:
    def __init__(self):
        self.clicks = 0
        self.isPressed = False

        self.root = ttk.Window(themename="solar")

        self.capybara1 = ttk.PhotoImage(file='static/capybara1.png')
        self.capybara2 = ttk.PhotoImage(file='static/capybara2.png')
        self.capybara3 = ttk.PhotoImage(file='static/capybara3.png')
        self.capybara4 = ttk.PhotoImage(file='static/capybara4.png')

        self.capybaraMainImg = self.capybara1

        self.capybaraButton = ttk.Button(self.root, text="Submit", image=self.capybaraMainImg, bootstyle=OUTLINE,
                                         command=self.click)
        self.capybaraButton.bind('<ButtonPress-1>', self.btnPress)
        self.capybaraButton.bind('<ButtonRelease-1>', self.btnUnpress)
        self.capybaraButton.pack(side=LEFT, padx=5, pady=10)

        self.text = ttk.Label(self.root, text="Hola!")
        self.text.pack(side=BOTTOM, padx=5, pady=10)

        self.root.mainloop()

    def click(self):
        self.clicks += 1
        self.text['text'] = f'{self.clicks} capybara coins'

    def btnPress(self, event):
        self.isPressed = True
        if self.capybaraMainImg == self.capybara1:
            self.capybaraMainImg = self.capybara2
        else:
            self.capybaraMainImg = self.capybara4

    def btnUnpress(self, event):
        self.isPressed = False
        if self.capybaraMainImg == self.capybara2:
            self.capybaraMainImg = self.capybara1
        else:
            self.capybaraMainImg = self.capybara3


if __name__ == '__main__':
    game = Game()
