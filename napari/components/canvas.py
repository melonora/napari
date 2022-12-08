from typing import Tuple

from napari.utils.events import EventedModel


class Canvas(EventedModel):
    size: Tuple[int, int] = (600, 800)
    show: bool = False
    bg_color: str = "#000000"
