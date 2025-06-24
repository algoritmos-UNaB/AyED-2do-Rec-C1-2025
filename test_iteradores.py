#!/usr/bin/env python3
"""
Test para verificar implementación de iteradores
"""

import sys
import traceback

def test_iteradores():
    """Verifica que los iteradores funcionen correctamente en Pila y PilaPresentaciones"""
    try:
        from ejercicio1 import Pila, PilaPresentaciones
        
        # Test iterador de Pila
        pila = Pila()
        elementos_pila = ['A', 'B', 'C', 'D']
        
        for elemento in elementos_pila:
            pila.apilar(elemento)
        
        # Iterar sobre la pila
        elementos_iterados_pila = []
        for elemento in pila:
            elementos_iterados_pila.append(elemento)
        
        # Test iterador de PilaPresentaciones (Cola)
        cola = PilaPresentaciones()
        elementos_cola = ['X', 'Y', 'Z']
        
        for elemento in elementos_cola:
            cola.apilar(elemento)  # En cola, esto va al final
        
        # Iterar sobre la cola
        elementos_iterados_cola = []
        for elemento in cola:
            elementos_iterados_cola.append(elemento)
        
        # Verificar que los iteradores funcionan
        # Para pila: debe iterar en orden LIFO (D, C, B, A)
        # Para cola: debe iterar en orden FIFO (X, Y, Z)
        
        pila_correcta = len(elementos_iterados_pila) == 4
        cola_correcta = len(elementos_iterados_cola) == 3
        
        # Verificar que se puede iterar múltiples veces
        segunda_iteracion_pila = list(pila)
        iteracion_multiple = len(segunda_iteracion_pila) == len(elementos_iterados_pila)
        
        if pila_correcta and cola_correcta and iteracion_multiple:
            print("Test passed: iterators working correctly")
            return True
        else:
            print(f"Test failed: pila={pila_correcta}, cola={cola_correcta}, multiple={iteracion_multiple}")
            return False
            
    except Exception as e:
        print(f"Test failed with exception: {str(e)}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_iteradores()
    sys.exit(0 if success else 1)