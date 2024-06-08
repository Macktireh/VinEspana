from customtkinter import CTkBaseClass
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

from config.settings import AssetsImages


class MapView(TkinterMapView):
    def __init__(self, master: CTkBaseClass, width: int, height: int) -> None:
        self.master = master

        super().__init__(master=master, width=width, height=height, corner_radius=8)

        # Load icons
        tinto_icon_img = Image.open(AssetsImages.TINTO).resize((35, 35))
        blanco_icon_img = Image.open(AssetsImages.BLANCO).resize((35, 35))
        self.tinto_icon = ImageTk.PhotoImage(tinto_icon_img)
        self.blanco_icon = ImageTk.PhotoImage(blanco_icon_img)

    def place_markers(self, data: dict) -> None:
        for region, (coords, wine_type) in data.items():
            icon = self.tinto_icon if wine_type == "Tinto" else self.blanco_icon
            self.set_marker(coords[0], coords[1], text=region, icon=icon)
