from tkinter import BOTH, LEFT, RIGHT

from customtkinter import CTkBaseClass, CTkFrame

from components.mapview import MapView
from components.sidebar import SideBar
from config.settings import DO_VINOS, Color


class HomeScreen(CTkFrame):
    def __init__(self, master: CTkBaseClass, width: int, height: int) -> None:
        self.master = master

        super().__init__(master=self.master, width=width, height=height, fg_color=Color.BG_CONTENT)

        self.sidebar = SideBar(master=self, width=width * 0.17, height=height)
        self.sidebar.pack(side=RIGHT, fill="y")

        self.sidebar.add_button("Espana", self.reset_zoom)
        for region, (coords, _) in DO_VINOS.items():
            self.sidebar.add_button(region, lambda c=coords: self.zoom_to_region(c))

        self.mapview = MapView(
            master=self,
            width=width * 0.8,
            height=height,
        )
        self.mapview.pack(fill=BOTH, expand=True, side=LEFT)
        self.mapview.set_position(40.4637, -3.7492)
        self.mapview.set_zoom(5)
        self.mapview.place_markers(DO_VINOS)

    def zoom_to_region(self, coords) -> None:
        self.mapview.set_position(coords[0], coords[1])
        self.mapview.set_zoom(10)

    def reset_zoom(self) -> None:
        self.mapview.set_position(40.4637, -3.7492)
        self.mapview.set_zoom(5)

