from tkinter import X

from customtkinter import CTkBaseClass, CTkFrame, CTkSwitch, StringVar, set_appearance_mode
from darkdetect import theme as get_system_theme

from config.settings import Color, Theme


class ThemeSwitcher(CTkFrame):
    def __init__(self, master: CTkBaseClass, default_theme: Theme = Theme.SYSTEM, **kwargs) -> None:
        super().__init__(master=master, fg_color=Color.BG_NAVIGATION, **kwargs)
        self._theme = default_theme.capitalize() if default_theme != Theme.SYSTEM else get_system_theme()

        self.theme_var = StringVar(value=self._theme)

        self.switch = CTkSwitch(
            master=self,
            text=f"{self._theme} Mode",
            command=self.change_theme,
            onvalue="Light",
            offvalue="Dark",
            variable=self.theme_var,
            progress_color=Color.BG_HOVER_BUTTON_NAVIGATION,
        )
        self.switch.pack(fill=X, padx=8, pady=5)
        self.change_theme()

    def change_theme(self) -> None:
        set_appearance_mode(self.theme_var.get().lower())
        self.switch.configure(text=f"{self.theme_var.get()} Mode")
