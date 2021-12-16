from .utils import get_abspath


def get_dark_theme():
    with open(get_abspath("assets", "theme", "dark.qss")) as f:
        return f.read()


def get_light_theme():
    with open(get_abspath("assets", "theme", "light.qss")) as f:
        return f.read()
