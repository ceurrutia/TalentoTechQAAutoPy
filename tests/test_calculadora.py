import pytest
from calculadora.operaciones import sumar, restar, multiplicar, dividir

def test_sumar_ok():
    assert sumar(2, 3) == 5

def test_restar_ok():
    assert restar(5, 2) == 3

def test_multiplicar_ok():
    assert multiplicar(4, 3) == 12

def test_dividir_ok():
    assert dividir(10, 2) == 5
    
def test_sumar_negativos():
    assert sumar(-1, 2) == "Error: No se permiten números negativos"


def test_dividir_por_cero():
    assert dividir(10, 0) == "Error: División por cero no permitida"