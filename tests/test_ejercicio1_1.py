import pytest
from src.P21.ejercicio1_1 import mayoredad

@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (6, False),
    (18, True),
    (3, False),
    (86, True),
    (2, False),
    (54, True),
    (8, False),
    (25, True),
    (7, False),
    (46, True),
    ]
)
def test_mayoredad_params(input_n1, expected):
    assert mayoredad(input_n1) == expected