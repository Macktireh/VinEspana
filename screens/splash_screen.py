from tkinter import Event, Frame, Label, PhotoImage, Tk

from config.settings import AssetsImages, Color, MetaData


class SplashScreen(Tk):
    WIDTH: int = 400
    HEIGHT: int = 200

    def __init__(self, app: Tk, duration: int) -> None:
        super().__init__()
        self.app = app
        self.duration = duration
        self.overrideredirect(True)
        self.update_idletasks()

        self._center_window()
        self.config(background=Color.BG_SPLASH)
        self.deiconify()

        self._display_exit_button()

        self.splach_logo = PhotoImage(file=AssetsImages.LOGO).subsample(7, 7)

        self.frame = Frame(self, background=Color.BG_SPLASH)
        self.frame.pack(expand=True, anchor="center")

        Label(self.frame, image=self.splach_logo, background=Color.BG_SPLASH, width=80, height=80).pack(pady=(0, 4))
        Label(self.frame, text=MetaData.APP_NAME, background=Color.BG_SPLASH, font=("Helvetica", 14)).pack()

    def _center_window(self) -> None:
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = SplashScreen.WIDTH + 2 * frm_width

        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = SplashScreen.HEIGHT + titlebar_height + frm_width

        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2

        self.geometry(f"{SplashScreen.WIDTH}x{SplashScreen.HEIGHT}+{x}+{y}")

    def _display_exit_button(self) -> None:
        self.BtnExit = Label(self, text="  X  ", font=("Arial", 13), background=Color.BG_SPLASH, fg="black", bd=1)
        self.BtnExit.place(relx=0.913, rely=0.001)
        self.BtnExit.bind("<Button-1>", lambda e: self.quit())

        for b in [self.BtnExit]:
            b.bind("<Enter>", self.change_bg_color)
            b.bind("<Leave>", self.change_fg_color)

    def change_bg_color(self, event: Event) -> None:
        self.BtnExit.config(background=Color.RED, fg=Color.WHITE, cursor="hand2")

    def change_fg_color(self, event: Event) -> None:
        self.BtnExit.config(background=Color.BG_SPLASH, fg=Color.BLACK)

    def run(self) -> None:
        self.after(self.duration, self.start_app)
        self.mainloop()

    def start_app(self) -> None:
        self.destroy()
        self.app().mainloop()
        self.quit()
