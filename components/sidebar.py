from collections.abc import Callable
from tkinter import TOP, W, X

from customtkinter import CTkBaseClass, CTkButton, CTkScrollableFrame

from config.settings import Color


class SideBar(CTkScrollableFrame):
    def __init__(self, master: CTkBaseClass, width: int, height: int) -> None:
        self.master = master
        self.__width = width
        self.btns = {}
        self.btn_active = None

        super().__init__(master=self.master, width=width, height=height, fg_color=Color.BG_NAVIGATION)

    def add_button(self, text: str, command: Callable) -> None:
        btn = CTkButton(
            master=self,
            text=text,
            width=self.__width * 0.6,
            command=command,
            fg_color=Color.BG_CARD,
            text_color=Color.TEXT,
            hover_color=Color.BG_HOVER_BUTTON_NAVIGATION,
            anchor=W,
        )
        btn.pack(side=TOP, fill=X, padx=8, pady=5)
        self.btns[text] = btn

    def set_active_button(self, region: str) -> None:
        if self.btn_active:
            self.btn_active.configure(fg_color=Color.BG_CARD)
        self.btn_active = self.btns[region]
        self.btn_active.configure(fg_color=Color.BG_ACTIVE_BUTTON_NAVIGATION)
