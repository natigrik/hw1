import pytest

from src.Triangle import Triangle
from src.Figure import Figure
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle


@pytest.fixture(params=[[2, 3, 4], [3, 4, 5]])
def triangle(request):
    return Triangle(request.param[0], request.param[1], request.param[2])


@pytest.fixture(params=[[0, 0, 0], [2, 3, 50], [2, 3, -4]])
def triangle_fail(request):
    return Triangle(request.param[0], request.param[1], request.param[2])


@pytest.fixture(params=[[5, 10], [2, 3]])
def rectangle(request):
    return Rectangle(request.param[0], request.param[1])


@pytest.fixture(params=[10])
def square(request):
    return Square(request.param)


@pytest.fixture(params=[3, 5])
def circle(request):
    return Circle(request.param)
