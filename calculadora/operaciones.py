def calculadora():
    print("Bienvenido a la calculadora")
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    while True:
        opcion = input("Ingrese el número de la operación que desea realizar: ")
        if opcion == "5":
            print("Gracias por usar la calculadora. Adios")
            break
        elif opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Solo se permiten números")
                continue
            
            if opcion == "1":
                resultado = sumar(num1, num2)
            elif opcion == "2":
                resultado = restar(num1, num2)
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
            elif opcion == "4":
                resultado = dividir(num1, num2)
                
            print(f"El resultado es: {resultado}")

## funciones
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

##print(calculadora())
       