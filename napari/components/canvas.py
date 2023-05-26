from typing import Tuple

import numpy as np

from napari.settings._application import GridHeight, GridStride, GridWidth
from napari.utils.events import EventedModel


class Canvas(EventedModel):
    grid_enabled: bool = False
    stride: GridStride = 1
    shape: Tuple[GridHeight, GridWidth] = (-1, -1)

    def actual_shape(self, nlayers: int = 1) -> Tuple[Tuple[int, int], int]:
        """Return the actual shape of the grid.

        This will return the shape parameter, unless one of the row
        or column numbers is -1 in which case it will compute the
        optimal shape of the grid given the number of layers and
        current stride.

        If the grid is not enabled, this will return (1, 1).

        Parameters
        ----------
        nlayers : int
            Number of layers that need to be placed in the grid.

        Returns
        -------
        shape : 2-tuple of int
            Number of rows and columns in the grid.
        """
        if not self.grid_enabled:
            return (1, 1), 0

        if nlayers == 0:
            return (1, 1), 0

        n_row, n_column = self.shape
        n_grid_squares = np.ceil(nlayers / abs(self.stride)).astype(int)

        if n_row == -1 and n_column == -1:
            n_column = np.ceil(np.sqrt(n_grid_squares)).astype(int)
            n_row = np.ceil(n_grid_squares / n_column).astype(int)
        elif n_row == -1:
            n_row = np.ceil(n_grid_squares / n_column).astype(int)
        elif n_column == -1:
            n_column = np.ceil(n_grid_squares / n_row).astype(int)

        n_row = max(1, n_row)
        n_column = max(1, n_column)

        return (n_row, n_column), n_grid_squares

    def position(self, index: int, nlayers: int) -> Tuple[int, int]:
        """Return the position of a given linear index in grid.

        If the grid is not enabled, this will return (0, 0).

        Parameters
        ----------
        index : int
            Position of current layer in layer list.
        nlayers : int
            Number of layers that need to be placed in the grid.

        Returns
        -------
        position : 2-tuple of int
            Row and column position of current index in the grid.
        """
        if not self.grid_enabled:
            return (0, 0)

        shape, n_gridboxes = self.actual_shape(nlayers)

        # Adjust for forward or reverse ordering
        adj_i = nlayers - index - 1 if self.stride < 0 else index

        adj_i = adj_i // abs(self.stride)
        adj_i = adj_i % (shape[0] * shape[1])
        i_row = adj_i // shape[1]
        i_column = adj_i % shape[1]
        return (i_row, i_column)
