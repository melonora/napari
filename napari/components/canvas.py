from typing import Optional, Tuple

import numpy as np

from napari.utils.events import EventedModel


class Canvas(EventedModel):
    size: Tuple[int, int] = (600, 800)
    bg_color: Optional[np.ndarray] = None
