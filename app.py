from tkinter import BOTH, RIGHT

from customtkinter import CTk

from config.settings import MetaData
from screens.home_screen import HomeScreen
from services.wine_service_impl import InMemoryWineService


class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title(MetaData.APP_NAME)
        self.minsize(MetaData.WIDTH * 0.65, MetaData.HEIGHT * 0.65)
        self._center_window()

        self.home_screen = HomeScreen(
            master=self,
            width=self._current_width,
            height=self._current_height,
            wine_service=InMemoryWineService(),
        )
        self.home_screen.pack(side=RIGHT, fill=BOTH, expand=True)

    def _center_window(self) -> None:
        """Center the application window on the screen."""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (MetaData.WIDTH // 2)
        y = (self.winfo_screenheight() // 2) - (MetaData.HEIGHT // 2)
        self.geometry(f"{MetaData.WIDTH}x{MetaData.HEIGHT}+{x}+{y}")
