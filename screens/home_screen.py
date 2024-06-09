from tkinter import BOTH, LEFT, RIGHT

from customtkinter import CTkBaseClass, CTkFrame

from components.mapview import MapView
from components.sidebar import SideBar
from config.settings import DO_VINOS, Color


class HomeScreen(CTkFrame):
    ESPANA = "Espana"

    def __init__(self, master: CTkBaseClass, width: int, height: int) -> None:
        self.master = master
        self.spanish_coords = (40.4637, -3.7492)

        super().__init__(master=self.master, width=width, height=height, fg_color=Color.BG_CONTENT)

        self.sidebar = SideBar(master=self, width=width * 0.17, height=height)
        self.sidebar.pack(side=RIGHT, fill="y")

        self.sidebar.add_button(self.ESPANA, lambda region=self.ESPANA: self.reset_zoom(region))
        for region, (coords, _) in DO_VINOS.items():
            self.sidebar.add_button(region, lambda c=coords, r=region: self.zoom_to_region(c, r))

        self.mapview = MapView(
            master=self,
            width=width * 0.8,
            height=height,
        )
        self.mapview.pack(fill=BOTH, expand=True, side=LEFT)
        self.reset_zoom(self.ESPANA)
        self.mapview.place_markers(DO_VINOS)

    def zoom_to_region(self, coords: tuple[float, float], region: str) -> None:
        self.sidebar.set_active_button(region)
        self.mapview.set_position(*coords)
        self.mapview.set_zoom(10)

    def reset_zoom(self, region: str) -> None:
        self.sidebar.set_active_button(region)
        self.mapview.set_position(*self.spanish_coords)
        self.mapview.set_zoom(5)
