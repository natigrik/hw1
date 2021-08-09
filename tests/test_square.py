import pytest


def test_create_square(square):
    assert square


# данный тест должен упасть, т.к. в классе Square специально не прописаны условия создания объекта
def test_fail_create_square(square_fail):
    assert square_fail is None


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_square_has_attribute(square, attribute):
    assert hasattr(square, attribute)


def test_square_area(square):
    s = square.side ** 2
    assert square.area == s.__round__(2)


def test_square_perimeter(square):
    per = square.side * 4
    assert square.perimeter == per.__round__(2)


# Не нашла, возможно ли передавать в параметры теста вызов фикстуры, поэтому отдельные тесты на все классы
def test_square_add_area_rectangle(square, rectangle):
    assert square.add_area(rectangle) == square.area + rectangle.area


def test_square_add_area_triangle(square, triangle):
    assert square.add_area(triangle) == square.area + triangle.area


def test_square_add_area_circle(square, circle):
    assert square.add_area(circle) == square.area + circle.area


def test_square_add_area_other(square, other):
    with pytest.raises(ValueError):
        square.add_area(other)
