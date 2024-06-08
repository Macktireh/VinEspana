from tkinter import BOTH, RIGHT

from customtkinter import CTk, set_appearance_mode

from config.settings import APP_NAME, Theme
from screens.home_screen import HomeScreen

set_appearance_mode(Theme.SYSTEM)


class App(CTk):
    width: int = 1024
    height: int = 600

    def __init__(self) -> None:
        super().__init__()
        self.title(APP_NAME)
        self.minsize(self.width * 0.65, self.height * 0.65)
        self.center_window()

        self.home_screen = HomeScreen(
            master=self,
            width=self._current_width,
            height=self._current_height,
        )
        self.home_screen.pack(side=RIGHT, fill=BOTH, expand=True)

    def center_window(self) -> None:
        """Center the application window on the screen."""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.winfo_screenheight() // 2) - (self.height // 2)
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
