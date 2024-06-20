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
    WINES_ICONS = {
        "Blanco": IMAGES_DIR / "blanco.webp",
        "Tinto": IMAGES_DIR / "tinto.webp",
    }


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


class Theme(StrEnum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"
