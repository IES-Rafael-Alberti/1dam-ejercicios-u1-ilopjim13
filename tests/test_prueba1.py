import pytest
from ..src.Pruebas.prueba1 import mayor

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (6, 3, 6),
    (3, 6, 6),
    (2, 4, 4),
    (8, 2, 8),
    (7, 8, 8),
    ]
)
def test_mayor_params(input_n1, input_n2, expected):
    assert mayor(input_n1, input_n2) == expected