import math


def test_create_triangle(triangle):
    assert triangle


def test_fail_create_triangle(triangle_fail):
    assert triangle_fail is None


def test_triangle_has_name(triangle):
    assert hasattr(triangle, "name")


def test_triangle_has_area(triangle):
    assert hasattr(triangle, "area")


def test_triangle_has_perimeter(triangle):
    assert hasattr(triangle, "perimeter")


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


# def test_create_square(square):
#     assert square
#
#
# def test_create_wrong_square(square):
#     assert square is None
#
#
# def test_create_rectangle(rectangle):
#     print(rectangle.first_side, rectangle.second_side)
#     assert rectangle
