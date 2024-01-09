# These tests would be for testing the layers itself
def test_get_layer_axes_labels():
    "For a given layer we should be able to retrieve axes labels."


def test_set_layer_axes_labels():
    "For a given layer we should be able to set the axes labels."


def test_default_axes_labels():
    """If no axes labels are given, default names should be assigned equal to the number of dimensions of a particular
    layer."""
    # Note that for broadcasting the default names should be based on negative integers, so ..., -2, -1.


def test_ndim_match_length_axes_labels():
    """The number of dimensions must match the length of axes labels when creating a layer and should throw an error
    if not the case"""


def test_slice_using_axes_labels():
    "We should be able to slice based on current axes labels and an interval."
