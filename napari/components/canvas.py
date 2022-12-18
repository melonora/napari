from typing import Optional, Tuple

import numpy as np

from napari.utils.events import EventedModel


class Canvas(EventedModel):
    status: str = ""
    mouse_over_canvas: bool = False
    size: Tuple[int, int] = (600, 800)
    show: bool = False
    bg_color: Optional[np.ndarray] = None
