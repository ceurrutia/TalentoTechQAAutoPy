
## CORRER LOS TESTS
## pytest -v
## pytest tests/test_calculadora.py --html=report.html

import pytest
from calculadora.operaciones import sumar, restar, multiplicar, dividir
from contest import numeros, num_negativos, num_div_zero

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