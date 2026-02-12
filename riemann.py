import math
# Samuel Cortez CI:31.841.128

def suma_riemann(f, a, b, n=100, tipo='izquierda'):
    """ Calcula la suma de Riemann"""
    h = (b - a) / n  # Ancho de cada rectángulo
    suma = 0.0
    
    for i in range(n):
        if tipo == 'izquierda':
            x = a + i * h
        elif tipo == 'derecha': 
            x = a + (i + 1) * h
        elif tipo == 'centro':
            x = a + (i + 0.5) * h 
        suma += f(x)  
    return suma * h

def calcular_integral(f, a, b, valor_real, n=100, tipo='izquierda'):
    """ Calcula valor aproximado, valor real y error """
    valor_aprox = suma_riemann(f, a, b, n, tipo)
    error = abs(valor_real - valor_aprox)
    error_relativo = abs((valor_real - valor_aprox) / valor_real) * 100
    return valor_aprox, valor_real, error, error_relativo

if __name__ == "__main__":
    # Ejemplo: ∫ x² dx desde 0 hasta 1 = 1/3
    mi_f = lambda x: x**2
    inf, sup = 0, 1
    valor_real = 1/3   # Valor exacto para calcular el error
    pasos = 100
    metodo = 'centro'
    
    try:
        aprox, real, error, error_rel = calcular_integral(mi_f, inf, sup, valor_real, 
                                                          n=pasos, tipo=metodo)
        print(f"Número de rectángulos: {pasos}")
        print(f"Límites: [{inf}, {sup}]")
        print("-" * 40)
        print(f"Valor aproximado: {aprox:.8f}")
        print(f"Valor real: {real:.8f}")
        print(f"Error absoluto: {error:.8f}")
        print(f"Error relativo: {error_rel:.4f}%")
        
    except Exception as e:
        print(f"Error: {e}")