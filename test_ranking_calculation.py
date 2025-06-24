#!/usr/bin/env python3
"""
Tests auxiliares para el sistema de autograding
Test específico para verificar cálculo de ranking
"""

import sys
import traceback

def test_ranking_calculation():
    """Prueba el cálculo correcto del ranking con múltiples presentaciones"""
    try:
        from ejercicio1 import Banda, PresentacionMusical
        
        # Crear banda de prueba
        banda = Banda("Test Band", ["Juan"], "Rock", "Buenos Aires")
        
        # Crear presentaciones con diferentes puntajes
        presentaciones = []
        puntajes = [450, 380, 420, 390, 410, 370, 440, 460, 350, 430]  # 10 presentaciones
        
        for i, puntaje in enumerate(puntajes):
            presentacion = PresentacionMusical(i+1, f"Evento {i+1}", f"Venue {i+1}", 500)
            presentacion.puntos_obtenidos = {"Test Band": puntaje}
            presentaciones.append(presentacion)
            banda.presentaciones.append(presentacion)
        
        # Calcular ranking (debe usar las mejores 8 de las 10)
        nuevo_ranking = banda.calcular_ranking(presentaciones)
        
        # Las mejores 8: 460, 450, 440, 430, 420, 410, 390, 380
        # Promedio esperado: (460+450+440+430+420+410+390+380)/8 = 422.5
        promedio_esperado = 422.5
        
        if abs(nuevo_ranking - promedio_esperado) < 0.1:
            print("Test passed: ranking calculation correct")
            return True
        else:
            print(f"Test failed: expected {promedio_esperado}, got {nuevo_ranking}")
            return False
            
    except Exception as e:
        print(f"Test failed with exception: {str(e)}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_ranking_calculation()
    sys.exit(0 if success else 1)