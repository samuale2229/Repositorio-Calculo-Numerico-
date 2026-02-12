import math
# Samuel Cortez CI:31.841.128

def newton_raphson(f, df, x0, er, n):
    """Algoritmo de Newton-Raphson.
    Args:
        f (function): función a calcularle la raíz.
        df (function): derivada de la función.
        x0 (float): valor inicial (aproximación inicial).
        er (float): cota máxima del error.
        n (int): número máximo de iteraciones.
    Returns:
        tuple: retorna una tupla con la raíz, el último error calculado y número de iteraciones
    """
    ei = 1.00           # Error iterativo.
    i = 0               # Contador de iteraciones.
    x_actual = x0       # Valor actual
    
    while (ei > er) and (i < n):
        # Calcular el siguiente valor
        x_siguiente = x_actual - f(x_actual) / df(x_actual)
        # Calcular el error relativo aproximado
        if x_siguiente != 0:
            ei = math.fabs((x_siguiente - x_actual) / x_siguiente)
        # Actualizar para la siguiente iteración
        x_actual = x_siguiente
        i = i + 1
    return x_actual, ei, i

if __name__ == "__main__":
    # prueba
    f = lambda x: math.exp(-x) - math.log(x)
    df = lambda x: -math.exp(-x) - 1/x  # Derivada de f(x)
    
    x0 = 1.3        # Valor inicial
    er = 0.01       # Tolerancia de error
    n = 100         # Número máximo de iteraciones
    # La función retorna 3 valores
    raiz, error, iteraciones = newton_raphson(f, df, x0, er, n)
    print(f"Raiz: {raiz:0.7f}")
    print(f"Error: {error:0.4f}")
    print(f"Iteraciones realizadas: {iteraciones}")