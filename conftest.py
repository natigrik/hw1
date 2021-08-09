import pytest

from src.Triangle import Triangle
from src.Figure import Figure
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle


# создание объектов с валидными параметрами
@pytest.fixture(scope="session", params=[[2, 3, 4], [3, 4, 5]])
def triangle(request):
    return Triangle(request.param[0], request.param[1], request.param[2])


@pytest.fixture(scope="session", params=[[5, 10], [2, 3]])
def rectangle(request):
    return Rectangle(request.param[0], request.param[1])


@pytest.fixture(scope="session", params=[10])
def square(request):
    return Square(request.param)


@pytest.fixture(scope="session", params=[3, 5])
def circle(request):
    return Circle(request.param)


# создание объектов с невалидными параметрами
@pytest.fixture(scope="session", params=[[0, 0, 0], [2, 30, 5], [2, 3, -4]])
def triangle_fail(request):
    return Triangle(request.param[0], request.param[1], request.param[2])


@pytest.fixture(scope="session", params=[[0, 0], [2, -4]])
def rectangle_fail(request):
    return Rectangle(request.param[0], request.param[1])


@pytest.fixture(scope="session", params=[0, -4])
def square_fail(request):
    return Square(request.param)


@pytest.fixture(scope="session", params=[0, -4])
def circle_fail(request):
    return Circle(request.param)


# создание объекта, не относящегося к классу Figure
@pytest.fixture(scope="session")
def other():
    other.name = 'other'
    other.area = 0
    other.perimeter = 0
    return other
