import pytest

@pytest.fixture
def numeros():
   return 10,2

@pytest.fixture
def num_negativos():
    return -10, -20

@pytest.fixture
def num_div_zero():
    return 20, 0