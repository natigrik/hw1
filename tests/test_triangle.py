import math
import pytest


def test_create_triangle(triangle):
    assert triangle


def test_fail_create_triangle(triangle_fail):
    assert triangle_fail is None


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_triangle_has_attribute(triangle, attribute):
    assert hasattr(triangle, attribute)


def test_triangle_area(triangle):
    p = (triangle.first_side + triangle.second_side + triangle.third_side) / 2
    s = math.sqrt(p * (p - triangle.first_side) * (p - triangle.second_side) * (p - triangle.third_side))
    assert triangle.area == s.__round__(2)


def test_triangle_perimeter(triangle):
    per = triangle.first_side + triangle.second_side + triangle.third_side
    assert triangle.perimeter == per.__round__(2)


def test_triangle_add_area_square(triangle, square):
    assert triangle.add_area(square) == triangle.area + square.area


def test_triangle_add_area_rectangle(triangle, rectangle):
    assert triangle.add_area(rectangle) == triangle.area + rectangle.area


def test_triangle_add_area_circle(triangle, circle):
    assert triangle.add_area(circle) == triangle.area + circle.area


def test_triangle_add_area_other(triangle, other):
    triangle.add_area(other)
    assert pytest.raises(ValueError)
