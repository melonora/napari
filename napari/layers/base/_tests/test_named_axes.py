import numpy as np
import pytest

from napari.layers import Image


# These tests would be for testing the layers itself
def test_get_layer_axes_labels():
    "For a given layer we should be able to retrieve axes labels."
    shape = (10, 15)
    np.random.seed(0)
    data = np.random.random(shape)
    layer = Image(data, axes_labels=("y", "x"))
    assert layer.axes_labels == ("y", "x")


def test_set_layer_axes_labels():
    "For a given layer we should be able to set the axes labels."
    shape = (10, 15)
    np.random.seed(0)
    data = np.random.random(shape)
    layer = Image(data, axes_label=("y", "x"))
    with pytest.raises(ValueError):
        layer.axes_labels = ("z", "y", "x")

    layer.axes_labels = ("z", "t")
    assert layer.axes_labels == ("z", "t")

    # Note: should we give a warning if reversing axes labels for example y,x to x, y


def test_default_axes_labels():
    """If no axes labels are given, default names should be assigned equal to the number of dimensions of a particular
    layer."""
    # Note that for broadcasting the default names should be based on negative integers, so ..., -2, -1.
    shape = (10, 15)
    data = np.random.random(shape)
    layer = Image(data)
    assert layer.axes_labels == (-2, -1)


def test_ndim_match_length_axes_labels():
    """The number of dimensions must match the length of axes labels when creating a layer and should throw an error
    if not the case"""


def test_slice_using_axes_labels():
    "We should be able to slice based on current axes labels and an interval."
