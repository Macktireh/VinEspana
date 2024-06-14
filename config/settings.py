from enum import StrEnum
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGES_DIR = BASE_DIR / "assets" / "images"


class MetaData:
    APP_NAME = "Vin España"
    WIDTH = 1024
    HEIGHT = 600
    COUNTRY_NAME = "Espana"
    COORDS = (40.4637, -3.7492)


class AssetsImages:
    ICON = IMAGES_DIR / "logo.ico"
    LOGO = IMAGES_DIR / "logo.png"
    BLANCO = IMAGES_DIR / "blanco.webp"
    TINTO = IMAGES_DIR / "tinto.webp"


class Theme(StrEnum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"


class Color:
    TRANSPARENT = "transparent"
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    GRAY = "#CCCCCC"
    RED = "#c60101"
    ORANGE = "#d97706"
    GREEN = "#017a01"
    BLUE = "#035fa1"
    TEXT = ("#000000", "#FFFFFF")
    TEXT_GRAY = ("#535050", "#9e9a9a")
    BG_CONTENT = ("#e0e0ff", "#2b2b31")
    BG_BUTON_DND = ("#d7d7fe", "#393941")
    BG_CONTENT_SECONDARY = ("#c2c2ff", "#393941")
    BG_NAVIGATION = ("#d2d2fe", "#333338")
    BG_BUTTON_NAVIGATION = "transparent"
    BG_ACTIVE_BUTTON_NAVIGATION = ("#5d5d98", "#545473")
    BG_HOVER_BUTTON_NAVIGATION = ("#6e6eaa", "#65658b")
    BG_CARD = ("#ccccff", "#31313a")
    BG_SPLASH = "#e0e0ff"
    BG_ALT_TREEVIEW = ("#ccccff", "#afafd5")


DO_VINOS = {
    "Alicante": ((38.3436365, -0.4881708), "Tinto"),
    "Calatayud": ((41.3527628, -1.6422977), "Tinto"),
    "Cariñena": ((41.3382122, -1.2263149), "Tinto"),
    "Condado de Huelva": ((37.3382055, -6.5384658), "Blanco"),
    "Jumilla": ((38.4735408, -1.3285417), "Tinto"),
    "La Gomera": ((28.116, -17.248), "Blanco"),
    "Málaga": ((36.7213028, -4.4216366), "Blanco"),
    "Rías Baixas": ((42.459627886165265, -8.722862824636783), "Blanco"),
    "Ribera del Duero": ((41.49232, -3.005), "Tinto"),
    "Rioja": ((42.29993373411561, -2.486288477690506), "Tinto"),
    "Rueda": ((41.4129785, -4.9597533), "Blanco"),
    "Somontano": ((42.0883878, 0.0994041), "Tinto"),
    "Tarragona": ((41.1172364, 1.2546057), "Tinto"),
    "Txakoli de Getaria": ((43.29428414467608, -2.202397625912913), "Blanco"),
    "Xérès": ((36.6816936, -6.1377402), "Blanco"),
}
