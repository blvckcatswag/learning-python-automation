import pytest
from lesson_16.homework_16_2 import Rectangle, Circle, Triangle


def test_rectangle_area_and_perimeter():
    r = Rectangle(4, 5)
    assert r.area() == 20
    assert r.perimeter() == 18


def test_circle_area_and_perimeter():
    c = Circle(7)
    assert round(c.area(), 2) == 153.94
    assert round(c.perimeter(), 2) == 43.98


def test_triangle_area_and_perimeter():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12
    assert t.area() == 6.0


def test_invalid_values_raise():
    with pytest.raises(ValueError):
        Rectangle(-1, 5)
    with pytest.raises(ValueError):
        Circle(0)
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)
