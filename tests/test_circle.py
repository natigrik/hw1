import pytest
import math


def test_create_circle(circle):
    assert circle


def test_fail_create_circle(circle_fail):
    assert circle_fail is None


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_circle_has_attribute(circle, attribute):
    assert hasattr(circle, attribute)


def test_circle_area(circle):
    s = (circle.radius ** 2) * math.pi
    assert circle.area == s.__round__(2)


def test_circle_perimeter(circle):
    per = circle.radius * 2 * math.pi
    assert circle.perimeter == per.__round__(2)


def test_circle_add_area_rectangle(circle, rectangle):
    assert circle.add_area(rectangle) == circle.area + rectangle.area


def test_circle_add_area_triangle(circle, triangle):
    assert circle.add_area(triangle) == circle.area + triangle.area


def test_circle_add_area_square(circle, square):
    assert circle.add_area(square) == circle.area + square.area
