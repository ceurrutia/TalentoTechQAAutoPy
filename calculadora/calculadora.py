def sumar(a,b):
    if a < 0 or b < 0:
        return "Error: No se permiten números negativos"
    if a == str or b == str:
        return "Error: Solo se permiten números"
    return a + b

def restar(a,b):
    if a < 0 or b < 0:
        return "Error: No se permiten números negativos"
    if a == str or b == str:
        return "Error: Solo se permiten números"
    return a - b

def multiplicar(a,b):
    if a < 0 or b < 0:
        return "Error: No se permiten números negativos"
    if a == str or b == str:
        return "Error: Solo se permiten números"
    
    return a * b

def dividir(a,b):
    if a < 0 or b < 0:
        return "Error: No se permiten números negativos"
    if a == str or b == str:
        return "Error: Solo se permiten números"
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"
    
print(sumar(-5, 3))
print(restar(5, 3))
print(multiplicar(5, 3))
print(dividir(5, 3))
print(dividir(5, 0))