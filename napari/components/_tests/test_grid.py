from napari.components.canvas import Canvas


def test_grid_creation():
    """Test creating grid object"""
    canvas = Canvas()
    assert canvas is not None
    assert not canvas.grid_enabled
    assert canvas.shape == (-1, -1)
    assert canvas.stride == 1


def test_shape_stride_creation():
    """Test creating grid object"""
    canvas = Canvas(shape=(3, 4), stride=2)
    assert canvas.shape == (3, 4)
    assert canvas.stride == 2


def test_actual_shape_and_position():
    """Test actual shape"""
    canvas = Canvas(grid_enabled=True)
    assert canvas.grid_enabled

    # 9 layers get put in a (3, 3) grid
    assert canvas.actual_shape(9) == ((3, 3), 9)
    assert canvas.position(0, 9) == (0, 0)
    assert canvas.position(2, 9) == (0, 2)
    assert canvas.position(3, 9) == (1, 0)
    assert canvas.position(8, 9) == (2, 2)

    # 5 layers get put in a (2, 3) grid
    assert canvas.actual_shape(5) == ((2, 3), 5)
    assert canvas.position(0, 5) == (0, 0)
    assert canvas.position(2, 5) == (0, 2)
    assert canvas.position(3, 5) == (1, 0)

    # 10 layers get put in a (3, 4) grid
    assert canvas.actual_shape(10) == ((3, 4), 10)
    assert canvas.position(0, 10) == (0, 0)
    assert canvas.position(2, 10) == (0, 2)
    assert canvas.position(3, 10) == (0, 3)
    assert canvas.position(8, 10) == (2, 0)


def test_actual_shape_with_stride():
    """Test actual shape"""
    canvas = Canvas(grid_enabled=True, stride=2)
    assert canvas.grid_enabled

    # 7 layers get put in a (2, 2) grid
    assert canvas.actual_shape(7) == ((2, 2), 4)
    assert canvas.position(0, 7) == (0, 0)
    assert canvas.position(1, 7) == (0, 0)
    assert canvas.position(2, 7) == (0, 1)
    assert canvas.position(3, 7) == (0, 1)
    assert canvas.position(6, 7) == (1, 1)

    # 3 layers get put in a (1, 2) grid
    assert canvas.actual_shape(3) == ((1, 2), 2)
    assert canvas.position(0, 3) == (0, 0)
    assert canvas.position(1, 3) == (0, 0)
    assert canvas.position(2, 3) == (0, 1)


def test_actual_shape_and_position_negative_stride():
    """Test actual shape"""
    canvas = Canvas(grid_enabled=True, stride=-1)
    assert canvas.grid_enabled

    # 9 layers get put in a (3, 3) grid
    assert canvas.actual_shape(9) == ((3, 3), 9)
    assert canvas.position(0, 9) == (2, 2)
    assert canvas.position(2, 9) == (2, 0)
    assert canvas.position(3, 9) == (1, 2)
    assert canvas.position(8, 9) == (0, 0)


def test_actual_shape_grid_disabled():
    """Test actual shape with grid disabled"""
    canvas = Canvas()
    assert not canvas.grid_enabled
    assert canvas.actual_shape(9) == ((1, 1), 0)
    assert canvas.position(3, 9) == (0, 0)
