import ttkbootstrap as tk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk


class MainWindow(tk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clicks = 0
        self.title('Capybara Game')
        self.geometry('800x600')

        self.shop_button = tk.Button(text='Открыть магазин', style=OUTLINE, command=self.open_shop)
        self.shop_button.pack(side=TOP, anchor=NE, pady=25, padx=25)

        self.clicksLabel = tk.Label(text='Кликай на капибару', font=('Helvetica', 24))
        self.clicksLabel.pack(side=BOTTOM, pady=25)

        # Загружаем и конвертируем изображение для кнопки
        self.original_image = Image.open('static/capybara-svgrepo-com.png').resize((200, 200))
        self.capybara_button_image = ImageTk.PhotoImage(self.original_image)

        # Создаем стиль для прозрачной кнопки
        capybara_button_style = tk.Style()

        # Стиль кнопки: Прозрачный фон (на самом деле фон окна), без границ
        capybara_button_style.configure(
            "Transparent.TButton",
            borderwidth=0,
            relief="flat",
            background=self["background"],  # Цвет совпадает с фоном окна (прозрачность имитируется)
            foreground="black",  # Цвет текста, если нужен
            highlightthickness=0,  # Убираем обводку при фокусе
            focuscolor=self["background"],  # Убираем цвет фокуса
            highlightbackground=self["background"]  # Убираем цвет фона для highlight
        )

        # Настройка эффектов при наведении и нажатии
        capybara_button_style.map(
            "Transparent.TButton",
            background=[("active", self["background"])],  # Убираем фон при наведении
            relief=[("pressed", "flat")],  # Убираем обводку после нажатия
            foreground=[("active", "black"), ("pressed", "black")]  # Цвет текста, если нужен
        )

        # Кнопка с изображением и кастомным стилем
        self.capybara_button = tk.Button(text='', image=self.capybara_button_image,
                                         style='Transparent.TButton', command=self.capybara_click)
        self.capybara_button.pack(side=BOTTOM, pady=25)

        # Привязка событий для затенения изображения
        self.capybara_button.bind("<ButtonPress>", self.on_button_press)
        self.capybara_button.bind("<ButtonRelease>", self.on_button_release)

    def on_button_press(self, event):
        # Затемняем изображение при нажатии
        darkened_image = self.original_image.convert("RGBA")
        for x in range(darkened_image.width):
            for y in range(darkened_image.height):
                r, g, b, a = darkened_image.getpixel((x, y))
                # Затемняем цвет на 50%
                darkened_image.putpixel((x, y), (int(r * 0.5), int(g * 0.5), int(b * 0.5), a))

        self.capybara_button_image = ImageTk.PhotoImage(darkened_image)
        self.capybara_button.config(image=self.capybara_button_image)

    def on_button_release(self, event):
        # Задержка перед возвратом к оригинальному изображению
        self.after(10, self.restore_image)

    def restore_image(self):
        # Возвращаем оригинальное изображение
        self.capybara_button_image = ImageTk.PhotoImage(self.original_image)
        self.capybara_button.config(image=self.capybara_button_image)

    def capybara_click(self):
        self.clicks += 1
        self.clicksLabel['text'] = f'{self.clicks} капибарных монет'

    def open_shop(self):
        self.withdraw()
        ShopWindow(self)


class ShopWindow(tk.Toplevel):
    def __init__(self, main_window: tk.Window, *args, **kwargs):
        super().__init__(master=main_window, *args, **kwargs)

        self.title('Capybara Shop')
        self.geometry('800x600')
        self.main_window = main_window

        self.protocol("WM_DELETE_WINDOW", self.close_shop_window)

        self.shop_button = tk.Button(text='Вернуться', style=OUTLINE, command=self.close_shop_window)
        self.shop_button.pack(side=TOP, anchor=NE, pady=25, padx=25)

    def close_shop_window(self):
        self.destroy()
        self.main_window.deiconify()


if __name__ == '__main__':
    root = MainWindow(themename='solar')
    root.mainloop()
