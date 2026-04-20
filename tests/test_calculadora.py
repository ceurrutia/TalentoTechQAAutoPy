
## CORRER LOS TESTS
## pytest -v
## pytest tests/test_calculadora.py --html=report.html

## pytest -m sumar -v

import pytest
from calculadora.operaciones import sumar, restar, multiplicar, dividir
from contest import numeros, num_negativos, num_div_zero

@pytest.mark.sumar
def test_sumar_ok(numeros):
    a, b = numeros
    assert sumar(a, b) == 12

def test_restar_ok(numeros):
    a, b = numeros
    assert restar(a, b) == 8

def test_multiplicar_ok(numeros):
    a, b = numeros
    assert multiplicar(a,b) == 20

def test_dividir_ok(numeros):
    a, b = numeros
    assert dividir(a, b) == 5
    
def test_sumar_negativos(num_negativos):
    a, b = num_negativos
    assert sumar(a, b) == "Error: No se permiten números negativos"


def test_dividir_por_cero(num_div_zero):
    a, b = num_div_zero
    assert dividir(a,b) == "Error: División por cero no permitida"
    
@pytest.mark.parametrize("a, b, resultado", [
    (10, 5, 15),
    (3, 7, 10),
    (1, 1, 2)
],
ids = ["caso 1", "caso 2", "caso 3"]
)

def test_sumar_parametrizado(a, b, resultado):
    assert sumar(a, b) == resultado

@pytest.mark.parametrize("a, b, resultado", [
    (10, 5, 5),     
    (3, 7, -4),     
    (1, 1, 0)
],
ids = ["caso 1", "caso 2", "caso 3"]
) 
def test_restar_parametrizado(a, b, resultado):
    assert restar(a, b) == resultado  