import math
# Samuel Cortez CI:31.841.128

def biseccion(f, a, b, er, n):
    """Algoritmo de Bisección.
    Args:
        f (function): función a calcularle la raíz.
        a (float): límite inferior del intervalo.
        b (float): límite superior del intervalo.
        er (float): cota máxima del error.
        n (int): número máximo de iteraciones.
    Returns:
        tuple: retorna una tupla con la raíz, el último error calculado y el número de iteraciones.
    """
    ei = 1.00           # Error iterativo.
    i = 0               # Contador de iteraciones.
    m_anterior = False  # Punto medio anterior.
    m_actual = 0        # Inicializar m_actual

    while (ei > er) and (i < n):
        m_actual = (a + b) / 2
        if m_anterior:
            ei = math.fabs((m_actual - m_anterior) / m_actual)
        if f(a) * f(m_actual) < 0:
            b = m_actual
        elif f(m_actual) * f(b) < 0:
            a = m_actual
        else:
            return m_actual, ei, i + 1  # Retorna iteración actual
        m_anterior = m_actual
        i = i + 1
    return m_actual, ei, i

if __name__ == "__main__":
    # ejemplo
    f = lambda x:  x**2 - 4
    a = 0
    b = 5
    er = 0.01
    n = 100

    raiz, error, iteraciones = biseccion(f, a, b, er, n)
    
    print(f"Raiz: {raiz:0.7f}")
    print(f"Error: {error:0.4f}")

    print(f"Iteraciones realizadas: {iteraciones}")
