# Versión interactiva: solicita números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
resultado = numero1 + numero2
print(f"La suma de {numero1} + {numero2} = {resultado}")

# Versión con función: reutilizable
def sumar(a, b):
    return a + b

# Ejemplo de uso de la función
print(sumar(5, 3))  # Salida: 8
