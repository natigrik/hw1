import pytest
from src.Figure import Figure


def test_create_figure():
    with pytest.raises(NotImplementedError):
        figure = Figure()
