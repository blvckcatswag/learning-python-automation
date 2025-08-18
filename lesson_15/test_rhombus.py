import pytest
from lesson_15.homework_15 import Rhombus


def test_angles_linked():
    r = Rhombus(5, angle_a=60)
    assert (r.angle_a, r.angle_b) == (60, 120)
    r.angle_b = 100
    assert (r.angle_a, r.angle_b) == (80, 100)


def test_side_validation():
    with pytest.raises(ValueError):
        Rhombus(0, angle_a=60)


def test_angles_sum_validation():
    with pytest.raises(ValueError):
        Rhombus(5, angle_a=100, angle_b=100)
