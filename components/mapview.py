from customtkinter import CTkBaseClass
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

from config.settings import AssetsImages


class MapView(TkinterMapView):
    def __init__(self, master: CTkBaseClass, width: int, height: int) -> None:
        self.master = master
        self.icons = {}

        super().__init__(master=master, width=width, height=height, corner_radius=8)

        for name, path in AssetsImages.WINES_ICONS.items():
            self.icons[name] = ImageTk.PhotoImage(Image.open(path).resize((35, 35)))

    def place_markers(self, data: dict) -> None:
        for region, (coords, wine_type) in data.items():
            self.set_marker(coords[0], coords[1], text=region, icon=self.icons[wine_type])
